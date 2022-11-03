# Homework 17 Flask-RESTX
___
### Creating DB:   
✅ Created tables: movies, directors, genres by using **SQLAlchemy**   
✅ Tables fill up from **data.py** file in directory **/data/**   
___
✅ **GET** requests:
- ***/movies/*** - return all movies   
- ***/movies/?director_id=2*** - return all movies, where attribute **director_id** is 2  
- ***/movies/?genre_id=4*** - return all movies, where attribute **genre_id** is 2  
- ***/movies/?director_id=2&genre_id=4*** - return all movies, where attribute **director_id** is 2 and attribute **genre_id** is 4  
- ***/directors/*** - return all directors   
- ***/genres/*** - return all genres   
- ***/movies/1*** - return movie with **id** = 1  
- ***/directors/1*** - return director with **id** = 1  
- ***/genres/1*** - return genre with **id** = 1   
_____
✅ **POST** requests:   
- ***/movies/*** - is called to add new movie   
- ***/director/*** - is called to add new director   
- ***/genres/*** - is called to add new genre   
___
✅ **PUT** requests (_index numbers are taken as an example_):   
- ***/movies/1*** - is called to update movie with **id** = 1   
- ***/directors/1*** - is called to update director with **id** = 1   
- ***/genres/1*** - is called to update genre with **id** = 1   
___
✅ **PATCH** requests (_index numbers are taken as an example_):     
- ***/movies/1*** - is called to partially update movie with **id** = 1   
- ***/directors/1*** - is called to partially update director with **id** = 1   
- ***/genres/1*** - is called to partially update genre with **id** = 1  
___
✅ **DELETE** requests (_index numbers are taken as an example_):     
- ***/movies/1*** - is called to delete movie with **id** = 1   
- ***/directors/1*** - is called to delete director with **id** = 1   
- ***/genres/1*** - is called to delete genre with **id** = 1  
___
✅ 404 error handler   
✅ 500 error handler   
___
✅ Requests testing done by using request-collection in Postman App

![requests](https://user-images.githubusercontent.com/106465054/199694485-6638edd1-6e6c-4f49-93ca-3e801d726dc5.png)
