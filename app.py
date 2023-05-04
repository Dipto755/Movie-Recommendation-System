import streamlit as st
from PIL import Image
import json
from KNN_Algo import KNearestNeighbours
from bs4 import BeautifulSoup
import requests,io
import PIL.Image
from urllib.request import urlopen



with open('movie_data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open('movie_title2.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)

def movie_poster_fetcher(imdb_link):
    url_data = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a056e7ae-f744-464e-a1e4-16cfd4a111f2',
            'url': imdb_link, 
        },
    )

    s_data = BeautifulSoup(url_data.text, "html.parser")
    
    imdb_dp = s_data.find("meta", property="og:image")
    movie_poster_link = imdb_dp.attrs['content']
    u = urlopen(movie_poster_link)
    raw_data = u.read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    image = image.resize((300, 500), )
    st.image(image, use_column_width=False)

def get_movie_info(imdb_link):
    
    url_data = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a056e7ae-f744-464e-a1e4-16cfd4a111f2',
            'url': imdb_link, 
        },
    )
    s_data = BeautifulSoup(url_data.text, 'html.parser')
    imdb_content = s_data.find("meta", property="og:description")
    movie_descr = imdb_content.attrs['content']
    movie_descr = str(movie_descr).split('.')
    movie_director = movie_descr[0]
    movie_cast = str(movie_descr[1]).replace('With', 'Cast: ').strip()
    if len(movie_descr) <3:
        movie_story = "None"
    else:
        movie_story = 'Story: ' + str(movie_descr[2]).strip()+'.'
    rating = s_data.find("div", class_="sc-bde20123-3 bjjENQ")
    print(rating)
    rating = str(rating).split('<div class="sc-bde20123-3 bjjENQ')
    rating = str(rating[1]).split("</div>")
    rating = str(rating[0]).replace(''' "> ''', '').replace('">', '')

    movie_rating = 'Total Rating count: '+ rating
    return movie_director,movie_cast,movie_story,movie_rating

def KNN_Movie_Recommender(test_point, k):
    
    target = [0 for item in movie_titles]
   
    model = KNearestNeighbours(data, target, test_point, k=k)
    
    model.fit()
    
    table = []
    for i in model.indices:

        table.append([movie_titles[i][1], movie_titles[i][4],data[i][-1]])
    print(table)
    return table

st.set_page_config(
   page_title="Movie Recommender System",page_icon="🎬"
)

