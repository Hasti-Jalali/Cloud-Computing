from flask import Flask, request
import json
from flask_cors import CORS, cross_origin
import Database
import Object_Storage as Obj
import os


app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'

db_dictionary = {
    'HOST': "mysql-2a3e420a-hastii-2c07.aivencloud.com",
    'PORT': 17752,
    'USER': "avnadmin",
    'PASSWORD': "AVNS_FLhMskMwQEoaul2OOjz",
    'DATABASE': "defaultdb"
}

db = Database.Database(db_dictionary)

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

    id = db.insert_data(email=email, description=description)
    
    image = request.files['image']
    file_extension = os.path.splitext(image.filename)[1]
    image.save(f'./Image Cache/{id}{file_extension}')

    return f'Please Remember Your Tracking Code: {id}'


# @app.route('/api/movies/<id>')
# @cross_origin()
# def get_movie(id):
#     movie = Movie_Top_Chart.query.get_or_404(id)
#     output = [{
#             'name': movie.name,
#             'id': str(movie.id),
#             'address1': movie.address1,
#             'address2': movie.address2,
#             'year': str(movie.year),
#             'director': movie.director,
#             'score': str(movie.score)
#         }]
#     # print(output)
#     # for movie in movies:
#     #     movie_data = {'name': movie.name, 'description': movie.description}
#     #     output.append(movie_data)
#     return json.dumps(output)

# @app.route('/api/topPicks')
# @cross_origin()
# def get_top_picks():
#     movies = Other_Movie.query.all()
#     output = []
#     for movie in movies:
#         if movie.type == 1:
#             output.append({
#                 'name': movie.name,
#                 'id': str(movie.id),
#                 'address': movie.address,
#                 'year': str(movie.year),
#             })
#     return json.dumps(output)

# @app.route('/api/fanFav')
# @cross_origin()
# def get_fan_fav():
#     movies = Other_Movie.query.all()
#     output = []
#     for movie in movies:
#         if movie.type == 2:
#             output.append({
#                 'name': movie.name,
#                 'id': str(movie.id),
#                 'address': movie.address,
#                 'year': str(movie.year),
#             })
#     return json.dumps(output)


# @app.route('/api/stream/<id>')
# @cross_origin()
# def start_stream(id):
#     # print('id', id)
#     # output = {'address': (f'./Videos/TopChartMpd/{id}/{id}.mpd')}
#     return f'./Videos/TopChartMpd/{id}/{id}.mpd'
