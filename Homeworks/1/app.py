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

    return f'لطفا کد پیگیری خود را به خاطر بسپارید: {id}'

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
        return f'آگهی شما با آیدی {id} در صف بررسی است.'

    if row[3] == 1:
        return f'آگهی شما با آیدی {id} رد شده است.'
    
    elif row[3] == 2:
        result = f"توضیحات: {row[1]}\n"
        result += f"دسته‌بندی {row[4]}\n"
        result += f"وضعیت {row[3]}\n"
        extention = row[6]
        file_name = Obj.S3().download_file(object_name=id, extention=extention)
        img = open(file_name, 'rb')
        # return make_response(result, img)
        return send_file(img, mimetype='image/jpeg'), result

