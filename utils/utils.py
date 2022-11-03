from app.models.models import db, Movie, Director, Genre
from flask import request, jsonify
from app.schemes import schemes as s


def create_database(app, data):
    """ This function creates database """
    with app.app_context():
        db.drop_all()
        db.create_all()
        load_movies(data)
        load_directors(data)
        load_genres(data)


def load_movies(data):
    """
    This function is called to create an objects of model Movie and load them to database
    :param data:
    :return:
    """
    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        with db.session.begin():
            db.session.add(m)


def load_directors(data):
    """
    This function is called to create an objects of model Director and load them to database
    :param data:
    :return:
    """
    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        with db.session.begin():
            db.session.add(d)


def load_genres(data):
    """
    This function is called to create an objects of model Genre and load them to database
    :param data:
    :return:
    """
    for genre in data["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        with db.session.begin():
            db.session.add(d)


def movies_get(did=None, gid=None, page=None):
    """
    This function takes parameters did and gid and filter movies by these parameters
    :param did: director_id
    :param gid: genre_id
    :param page: number of page
    :return: filtered list of movies if gid and did are None, else return all movies
    """
    if did and not gid:
        movies = Movie.query.filter_by(director_id=did)
        return s.movies_schema.dump(movies)
    if gid and not did:
        movies = Movie.query.filter_by(genre_id=gid)
        return s.movies_schema.dump(movies)
    if did and gid:
        movies = db.session.query(Movie).filter(
            Movie.genre_id == gid, Movie.director_id == did)
        return s.movies_schema.dump(movies)
    else:
        if page and int(page) > 0:
            all_movies = db.session.query(Movie).limit(5).offset(int(page) - 1)
            return s.movies_schema.dump(all_movies)


def movie_get(mid):
    """
    This function is called to get movie by movie_id
    :param mid: movie_id
    :return: movie by movie_id
    """
    try:
        movie = db.session.query(Movie).filter(Movie.id == mid).one()
        return s.movie_schema.dump(movie)
    except Exception as e:
        return str(e)


def movie_post():
    """
    This function is called to add new movie
    :return:
    """
    req_json = request.json
    new_movie = Movie(**req_json)
    with db.session.begin():
        db.session.add(new_movie)
        db.session.commit()
    return ""


def movie_put(mid):
    """
    This function is called to update a movie, chosen by movie_id
    :param mid: movie_id
    :return: updated movie
    """
    movie = db.session.query(Movie).get(mid)
    req_json = request.json
    movie.title = req_json.get('title')
    movie.description = req_json.get('description')
    movie.trailer = req_json.get('trailer')
    movie.year = req_json.get('year')
    movie.rating = req_json.get('rating')
    movie.genre_id = req_json.get('genre_id')
    movie.director_id = req_json.get('director_id')
    db.session.add(movie)
    db.session.commit()
    return ""


def movie_patch(mid):
    """
    This function is called to partially update a movie, chosen by movie id
    :param mid: movie_id
    :return: partially updated movie
    """
    movie = db.session.query(Movie).get(mid)
    req_json = request.json
    if "title" in req_json:
        movie.title = req_json.get('title')
    if "description" in req_json:
        movie.description = req_json.get('description')
    if "trailer" in req_json:
        movie.trailer = req_json.get('trailer')
    if "year" in req_json:
        movie.year = req_json.get('year')
    if "rating" in req_json:
        movie.rating = req_json.get('rating')
    if "genre_id" in req_json:
        movie.genre_id = req_json.get('genre_id')
    if "director_id" in req_json:
        movie.director_id = req_json.get('director_id')
    db.session.add(movie)
    db.session.commit()
    return ""


def movie_delete(mid):
    """
    This function is called to delete a movie, chosen by movie_id, from database
    :param mid: movie_id
    :return:
    """
    movie = db.session.query(Movie).get(mid)
    db.session.delete(movie)
    db.session.commit()
    return ""


def director_post():
    """
    This function is called to add new director to database
    :return:
    """
    req_json = request.json
    new_director = Director(**req_json)
    with db.session.begin():
        db.session.add(new_director)
        db.session.commit()
    return ""


def director_get(did):
    """
    This function is called to get the director by director_id
    :param did: director_id
    :return: director by director_id and list of films
    """
    director_dict = {}
    try:
        movies = db.session.query(Movie.title, Movie.rating, Movie.year, Movie.trailer, Movie.description). \
            join(Director, Director.id == Movie.director_id).filter(Director.id == did)
        genre = db.session.query(Director).filter(Director.id == did).one()
        director_dict[s.director_schema.dump(genre).get('name')] = s.movies_schema.dump(movies)
        return director_dict
    except Exception as e:
        return str(e)


def director_put(did):
    """
    This function is called to update the director, chosen by director_id
    :param did: director_id
    :return: updated director object
    """
    director = db.session.query(Director).get(did)
    req_json = request.json
    director.name = req_json.get('name')
    db.session.add(director)
    db.session.commit()
    return ""


def director_patch(did):
    """
    This function is called to partially update the director, chosen by director_id
    :param did: director_id
    :return: partially updated director
    """
    director = db.session.query(Director).get(did)
    req_json = request.json
    if "name" in req_json:
        director.name = req_json.get("name")
    db.session.add(director)
    db.session.commit()
    return ""


def director_delete(did):
    """
    This function is called to delete the director, chosen by director_id
    :param did: director_id
    :return:
    """
    director = db.session.query(Director).get(did)
    db.session.delete(director)
    db.session.commit()
    return ""


def genre_post():
    """
    This function is called to add a new genre to database
    :return:
    """
    req_json = request.json
    new_genre = Genre(**req_json)
    with db.session.begin():
        db.session.add(new_genre)
        db.session.commit()
    return ""


def genre_get(gid):
    """
    This function is called to get genre and a list of films with this genre, chosen by genre_id
    :param gid: genre_id
    :return: genre and list of films
    """
    genre_dict = {}
    try:
        movies = db.session.query(Movie.title, Movie.rating, Movie.year, Movie.trailer, Movie.description).\
            join(Genre, Genre.id == Movie.genre_id).filter(Genre.id == gid)
        genre = db.session.query(Genre).filter(Genre.id == gid).one()
        genre_dict[s.genre_schema.dump(genre).get('name')] = s.movies_schema.dump(movies)
        return genre_dict
    except Exception as e:
        return str(e)


def genre_put(gid):
    """
    This function is called to update genre, chosen by genre_id
    :param gid: genre_id
    :return: updated genre by genre_id
    """
    genre = db.session.query(Genre).get(gid)
    req_json = request.json
    genre.name = req_json.get('name')
    db.session.add(genre)
    db.session.commit()
    return ""


def genre_patch(gid):
    """
    This function is called to partially update a genre, chosen by genre_id
    :param gid: genre_id
    :return: partially updated genre
    """
    genre = db.session.query(Genre).get(gid)
    req_json = request.json
    if "name" in req_json:
        genre.name = req_json.get("name")
    db.session.add(genre)
    db.session.commit()
    return ""


def genre_delete(gid):
    """
    This function is called to delete a genre, chosen by genre_id
    :param gid: genre_id
    :return:
    """
    genre = db.session.query(Genre).get(gid)
    db.session.delete(genre)
    db.session.commit()
    return ""
