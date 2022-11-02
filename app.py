from flask import Flask, request
from flask_restx import Resource, Api
from app.models.models import db, Director, Genre
from app.schemes import schemes as s
from utils import utils as u
from data.data import data


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# create database
u.create_database(app, data)

api = Api(app)

# register namespaces
movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    def get():
        """This view returns all movies or movies, filtered by director_id or/and genre_id"""
        did = request.args.get('director_id')
        gid = request.args.get('genre_id')
        return u.movies_get(did, gid), 200

    @staticmethod
    def post():
        """This view adds a new movie"""
        return u.movie_post(), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @staticmethod
    def get(mid: int):
        """This view returns a movie by movie_id"""
        return u.movie_get(mid), 200

    @staticmethod
    def put(mid: int):
        """This view updates a movie by movie_id"""
        return u.movie_put(mid), 204

    @staticmethod
    def patch(mid: int):
        """This view partially updates a movie by movie_id"""
        return u.movie_patch(mid), 204

    @staticmethod
    def delete(mid: int):
        """This view deletes a movie by movie_id"""
        return u.movie_delete(mid), 204


@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        """This view returns all directors"""
        all_directors = db.session.query(Director).all()
        return s.directors_schema.dump(all_directors), 200

    @staticmethod
    def post():
        """This view adds a new director"""
        return u.director_post(), 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @staticmethod
    def get(did: int):
        """This view returns the director by director_id"""
        return u.director_get(did), 200

    @staticmethod
    def put(did: int):
        """This view updates the director by director_id"""
        return u.director_put(did), 204

    @staticmethod
    def patch(did: int):
        """This view partially updates the director by director_id"""
        return u.director_patch(did), 204

    @staticmethod
    def delete(did: int):
        """This view deletes the director by director_id"""
        return u.director_delete(did), 204


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        """This view returns all genres"""
        genres = db.session.query(Genre).all()
        return s.genres_schema.dump(genres), 200

    @staticmethod
    def post():
        """This view adds a new genre"""
        return u.genre_post(), 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @staticmethod
    def get(gid: int):
        """This view returns a genre by genre id"""
        return u.genre_get(gid), 200

    @staticmethod
    def put(gid: int):
        """This view updates a genre by genre id"""
        return u.genre_put(gid), 204

    @staticmethod
    def patch(gid: int):
        """This view partially updates a genre by genre id"""
        return u.genre_patch(gid), 204

    @staticmethod
    def delete(gid: int):
        """This view deletes a genre by genre id"""
        return u.genre_delete(gid), 204


@app.errorhandler(404)
def get_404_error(error):
    """This view is a 404 error handler"""
    return '404 Error', 404


@app.errorhandler(500)
def get_500_error(error):
    """This view is a 500 error handler"""
    return '500 Error', 500


if __name__ == '__main__':
    app.run(debug=True)
