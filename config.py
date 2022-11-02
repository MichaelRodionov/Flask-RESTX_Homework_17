from os import path


SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.abspath(path.join("data", "movies.db"))}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_AS_ASCII = False
