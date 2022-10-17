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

    response = requests.get(
        MOVIE_API_BASE_URL,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )
    json_data = response.json()

    this_movie = json_data
    movie_data = this_movie['title']

    print(movie_data)

get_movies()

app = flask.Flask(__name__)
app.secret_key = 'lmtlmtlmt'

@app.route('/')
def wesbite_title():
    return flask.render_template('website.html')

app.run(debug=True)
