from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movie_Trailer'
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)

cors = CORS(app, resources={r'/api/*': {"origins": "*"}})

# print(Stream().start(1))

class Movie_Top_Chart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address1 = db.Column(db.String(300))
    address2 = db.Column(db.String(300))
    year = db.Column(db.Integer)
    director = db.Column(db.String(120))
    score = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"{self.name} - {self.address1} - {self.director} - {self.year}"


class Other_Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(300))
    year = db.Column(db.Integer)
    director = db.Column(db.String(120))
    score = db.Column(db.Float)
    type = db.Column(db.Integer) #if type=1 => top_picks else fan_favourite
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.address} - {self.director} - {self.year}"

# db.create_all()
# db.session.commit()
# db.session.add(Movie_Top_Chart(name='The Shawshank Redemption', address1='/public/movieassets/TopCharts/01.jpg', address2='/public/movieassets/TopCharts/01p.jpg',year=1994, director='Frank Darabont', score=9.2))
# db.session.add(Movie_Top_Chart(name='The Godfather', address1='/public/movieassets/TopCharts/02.jpg', address2='/public/movieassets/TopCharts/02p.jpg',year=1972, director='Francis Ford Coppola', score=9.2))
# db.session.add(Movie_Top_Chart(name='The Dark Knight',address1='/public/movieassets/TopCharts/03.jpg', address2='/public/movieassets/TopCharts/03p.jpg',year=2008, director='Christopher Nolan', score=9.0))
# db.session.add(Movie_Top_Chart(name='The Godfather Part II', address1='/public/movieassets/TopCharts/04.jpg', address2='/public/movieassets/TopCharts/04p.jpg',year=1974, director='Francis Ford Coppola', score=9.0))
# db.session.add(Movie_Top_Chart(name='12 Angry Men', address1='/public/movieassets/TopCharts/05.jpg', address2='/public/movieassets/TopCharts/05p.jpg',year=1957, director='Sidney Lumet', score=8.9))
# db.session.add(Movie_Top_Chart(name="Schindler's List", address1='/public/movieassets/TopCharts/06.jpg', address2='/public/movieassets/TopCharts/06p.jpg',year=1993, director='Steven Spielberg', score=8.9))

# # Top picks
# db.session.add(Other_Movie(name='Good Will Hunting', address='/public/movieassets/TopPicks/01.jpg',year=1997, type=1))
# db.session.add(Other_Movie(name='Inception', address='/public/movieassets/TopPicks/02.jpg',year=2010, type=1))
# db.session.add(Other_Movie(name='Lord Of The Rings: The Fellowship Of The Ring', address='/public/movieassets/TopPicks/03.jpg',year=2001, type=1))
# db.session.add(Other_Movie(name='House Of Gucci', address='/public/movieassets/TopPicks/04.jpg',year=2021, type=1))
# db.session.add(Other_Movie(name='Fight Club', address='/public/movieassets/TopPicks/05.jpg',year=1999, type=1))
# db.session.add(Other_Movie(name='Nightmare Alley', address='/public/movieassets/TopPicks/06.jpg',year=2021, type=1))
# db.session.add(Other_Movie(name='Goodfellas', address='/public/movieassets/TopPicks/06.jpg',year=1990, type=1))

# # Fan favourite
# db.session.add(Other_Movie(name='Sherlock', address='/public/movieassets/FanFavourite/01.jpg',year=2010, type=2))
# db.session.add(Other_Movie(name='Star Wars: Revenge Of The Sith', address='/public/movieassets/FanFavourite/02.jpg',year=2005, type=2))
# db.session.add(Other_Movie(name='Stranger Things', address='/public/movieassets/FanFavourite/03.jpg',year=2016, type=2))
# db.session.add(Other_Movie(name='The Boys', address='/public/movieassets/FanFavourite/04.jpg',year=2019, type=2))
# db.session.add(Other_Movie(name='Top Gun Maverick', address='/public/movieassets/FanFavourite/05.jpg',year=2022, type=2))

# db.session.commit()
# Movie_Top_Chart.query.all()

@app.route('/')
@cross_origin()
def index():
    return 'Hello!'


@app.route('/api/movies')
@cross_origin()
def get_movies():
    movies = Movie_Top_Chart.query.all()
    output = []
    for movie in movies:
        output.append({
            'name': movie.name,
            'id': str(movie.id),
            'address1': movie.address1,
            'address2': movie.address2,
            'year': str(movie.year),
            'director': movie.director,
            'score': str(movie.score)
        })
    # print(output)
    # for movie in movies:
    #     movie_data = {'name': movie.name, 'description': movie.description}
    #     output.append(movie_data)
    return json.dumps(output)

@app.route('/api/movies/<id>')
@cross_origin()
def get_movie(id):
    movie = Movie_Top_Chart.query.get_or_404(id)
    output = [{
            'name': movie.name,
            'id': str(movie.id),
            'address1': movie.address1,
            'address2': movie.address2,
            'year': str(movie.year),
            'director': movie.director,
            'score': str(movie.score)
        }]
    # print(output)
    # for movie in movies:
    #     movie_data = {'name': movie.name, 'description': movie.description}
    #     output.append(movie_data)
    return json.dumps(output)

@app.route('/api/topPicks')
@cross_origin()
def get_top_picks():
    movies = Other_Movie.query.all()
    output = []
    for movie in movies:
        if movie.type == 1:
            output.append({
                'name': movie.name,
                'id': str(movie.id),
                'address': movie.address,
                'year': str(movie.year),
            })
    return json.dumps(output)

@app.route('/api/fanFav')
@cross_origin()
def get_fan_fav():
    movies = Other_Movie.query.all()
    output = []
    for movie in movies:
        if movie.type == 2:
            output.append({
                'name': movie.name,
                'id': str(movie.id),
                'address': movie.address,
                'year': str(movie.year),
            })
    return json.dumps(output)


@app.route('/api/stream/<id>')
@cross_origin()
def start_stream(id):
    # print('id', id)
    # output = {'address': (f'./Videos/TopChartMpd/{id}/{id}.mpd')}
    return f'./Videos/TopChartMpd/{id}/{id}.mpd'
