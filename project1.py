from urllib import response
import flask
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
from random import randrange

load_dotenv(find_dotenv())

def get_movies():
    
    MOVIE_IDS = [10719, 50014, 222935]
    MOVIE_PATH = f'/movie/{MOVIE_IDS[randrange(3)]}'
    MOVIE_API_BASE_URL = f'https://api.themoviedb.org/3{MOVIE_PATH}'
    #WIKI_IMAGE_URL = ''

    response = requests.get(
        MOVIE_API_BASE_URL,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )

    this_movie = response.json()
    genres_of_movie = ""
    for genre in response['genres']:
        genres_of_movie += str(genre['name']) + ", "

    movie_info = [this_movie['original_title'], this_movie['overview']]
    
    return movie_info
    #print(movie_info)

app = flask.Flask(__name__)
#app.secret_key = 'lmtlmtlmt'

@app.route('/')
def website_title():
    get_movies();
    return flask.render_template('website.html')

app.run()
