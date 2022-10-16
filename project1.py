import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

def get_top_10_weekly_trending_movies():
    
    TMDB_TRENDING_MOVIES_API_BASE_URL = 'https://api.themoviedb.org/3/trending/movie/week'
    
    response = requests.get(
        TMDB_TRENDING_MOVIES_API_BASE_URL,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )

    json_data = response.json()   
    weekly_trending_movie_object = json_data
    weekly_trending_movie_list = weekly_trending_movie_object['results']

    for i in range(10):
        print(weekly_trending_movie_list[i]['title'])
        
get_top_10_weekly_trending_movies()