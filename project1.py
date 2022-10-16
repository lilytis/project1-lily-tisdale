from urllib import response
#import flask
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
from random import randrange

load_dotenv(find_dotenv())

def get_movies():
    
    MOVIE_IDS = [157336, 14836, 646385]
    MOVIE_PATH = f'/movie/{MOVIE_IDS[randrange(3)]}'
    MOVIE_API_BASE_URL = f'https://api.themoviedb.org/3{MOVIE_PATH}'

    response = requests.get(
        MOVIE_API_BASE_URL,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )
    json_data = response.json()

    movie_1 = json_data
    movie_1_data = movie_1['title']

    print(movie_1_data)

get_movies()
