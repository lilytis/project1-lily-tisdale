from urllib import response
import flask
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
from random import randrange

load_dotenv(find_dotenv())

def get_movies():
    
    MOVIE_IDS = [642885, 616820, 760161]
    MOVIE_PATH = f'/movie/{MOVIE_IDS[randrange(3)]}'
    MOVIE_API_BASE_URL = f'https://api.themoviedb.org/3{MOVIE_PATH}'
    IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

    response = requests.get(
        MOVIE_API_BASE_URL,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )

    this_movie = response.json()
    image_path = IMAGE_URL + this_movie['poster_path']
    genres_of_movie = ""
    for genre in this_movie['genres']:
        genres_of_movie += str(genre['name']) + ", "

    wiki_url = get_wiki_url(title = this_movie['original_title'])
    movie_info = [this_movie['original_title'], this_movie['tagline'],
                    genres_of_movie, image_path, wiki_url]

    return movie_info

app = flask.Flask(__name__)
#app.secret_key = 'lmtlmtlmt'

def get_wiki_url(title):
    request = requests.Session()

    WIKI_URL = "https://en.wikipedia.org/w/api.php"

    params = {
        "action":"opensearch",
        "namespace":"0",
        "search": str(title), #+ "movie"
        "limit":"1",
        "format":"json"
    }

    wiki_info = request.get(url=WIKI_URL, params=params)
    get_info = wiki_info.json()
    return get_info[3][0]

@app.route('/')
def website_title():
    list_of_movie_info = get_movies()
    return flask.render_template('website.html', title=list_of_movie_info[0], tagline=list_of_movie_info[1], genres=list_of_movie_info[2], image=list_of_movie_info[3], link=list_of_movie_info[4])

#app.run(debug=True)
