from flask import Flask, request, send_file
import json
from flask_cors import CORS, cross_origin
import Database
import Object_Storage as Obj
import os
import RabbitMQ_Send

app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'



db = Database.Database()

# cors = CORS(app, resources={r'/api/*': {"origins": "*"}})

# print(Stream().start(1))

@app.route('/test/')
# @cross_origin()
def index():
    return 'Hello World!'


@app.route('/addPost/', methods=['POST'])
def addPost():

    email = request.form.get("email")
    description = request.form.get("description")
    image = request.files['image']
    file_extension = os.path.splitext(image.filename)[1]
    id = db.insert_data(email=email, description=description, extention=file_extension)
    
    file_path = f'./Image Cache/{id}{file_extension}'
    image.save(file_path)
    Obj.S3().upload_file(file_path)
    os.remove(file_path) 
    RabbitMQ_Send.rabbitMQ_send().send_message(f"{id}{file_extension}")

    return f'Pleas remember your id: {id} for tracking your advertisement'


@app.route('/postTracking/', methods=['POST'])
def postTracking():

    id = request.form.get("id")

    row = db.select_by_id(id)[0]
    # print(row)
    '''
    row[0] = id
    row[1] = description
    row[2] = email
    row[3] = state
    row[4] = category
    row[6] = extention
    '''
    if row[3] == 0:
        return f'Your Advertisement with id: {id} is pending'

    if row[3] == 1:
        return f'Your Advertisement with id: {id} is rejected'
    
    elif row[3] == 2:
        result = f"description: {row[1]}\n"
        result += f"category: {row[4]}\n"
        result += f"state: Your Advertisement with id: {id} is approved\n"
        extention = row[6]
        url = Obj.S3().get_url(f'{id}{extention}')
        result += f"url: {url}\n"
        return result
