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
def run():
    def add_bg_from_url():
        st.markdown(
            f"""
                     <style>
                     .stApp {{
                         background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
                         background-attachment: fixed;
                         background-size: cover

                     }}
                     </style>
                     """,
            unsafe_allow_html=True)
    add_bg_from_url()
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    activities = ["About Project", "Project Github Link", "About Us"]
    choice = st.sidebar.selectbox("Project Details Section", activities)

    if choice == 'About Project':
            st.sidebar.write(
                "This is a movie Recommendation System when you select an movie then it will recommend 5 movies which are similar to the selected movie. I made this project by using of Python programming language and sstreamlit. ")


    elif choice == 'Project Github Link':
            st.sidebar.write("Click Here")
            st.sidebar.write("[LinkedIn Profile](https://github.com/Dipto755/Movie-Recommendation-System)")

    elif choice == 'About Us':
        st.sidebar.write("Md.Akteruzzaman Dipto")
        st.sidebar.write("Ayesha Nasiba")
        st.sidebar.write("Tabassum Chowdhury")


    st.write("<h1 style='text-align: center; color: #D1051E; font-family:Serif '> MOVIE RECOMMENDATION SYSTEM</h1>",
             unsafe_allow_html=True)
    
    genres = ['Action','Adult','Adventure','Animation','Biography','Comedy','Crime',
              'Documentary','Drama','Family','Fantasy','Film-Noir','Game-Show','History',
              'Horror','Music','Musical','Mystery','News','Reality-TV','Romance','Sci-Fi',
              'Short','Sport','Talk-Show','Thriller','War','Western']
    movies = [title[1] for title in movie_titles]
    category = ['--Select--', 'Movie based', 'Genre based']
    cat_op = st.selectbox('Select Recommendation Type', category)
    if cat_op == category[0]:
        st.warning('Please select Recommendation Type!!')
    elif cat_op == category[1]:
        select_movie = st.selectbox('Select movie: (Recommendation will be based on this selection)', ['--Select--'] + movies)
        dec = st.radio("Want to Fetch Movie Poster?", ('Yes', 'No'))
        st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Fetching a Movie Posters will take a time."</h4>''',
                    unsafe_allow_html=True)
        if dec == 'No':
            pass
        else:
            if select_movie == '--Select--':
                st.warning('Please select Movie!!')
            else:
                no_of_reco = st.slider('Number of movies you want Recommended:', min_value=5, max_value=20, step=1)
                genres = data[movies.index(select_movie)]
                test_points = genres
                table = KNN_Movie_Recommender(test_points, no_of_reco+1)
                table.pop(0)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                streamlit_style = """
                                  			<style>
                                             @import url('https://fonts.googleapis.com/css2?family=PT+Serif&display=swap');
                                  			html, body, [class*="css"]  {
                                  			# font-family: 'Roboto', sans-serif;
                                  			font-family: 'PT Serif', serif;

                                  			}
                                  			</style>
                                  			"""
                st.markdown(streamlit_style, unsafe_allow_html=True)


                i=0;
                for movie, link, ratings in table:
                    c += 1
                    if i%2== 0:
                    # print(link)
                      cols1, cols2 = st.columns(2)
                      with cols1:
                         movie_poster_fetcher(link)


                      with cols2:
                        director, cast, story, total_rat = get_movie_info(link)

                        st.title(movie)
                        st.write(director)
                        st.write(cast)
                        st.write(story)
                      # st.markdown(total_rat)
                        st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
                        st.write(f"(imdb link)[ {movie}]({link})")
                      st.write("\n")
                      st.write(" \n")
                      st.write("  \n")
                      st.write("\n")
                      st.write(" \n")
                      st.write("  \n")
                    else:
                        cols1, cols2 = st.columns(2)
                        with cols1:
                            director, cast, story, total_rat = get_movie_info(link)
                            st.title(movie)
                            st.write(director)
                            st.write(cast)
                            st.write(story)
                            # st.markdown(total_rat)
                            st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
                            st.write(f"(imdb link)[ {movie}]({link})")


                        with cols2:

                            movie_poster_fetcher(link)

                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                    i+=1

    elif cat_op == category[2]:
        sel_gen = st.multiselect('Select Genres:', genres)
        dec = st.radio("Want to Fetch Movie Poster?", ('Yes', 'No'))
        st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Fetching a Movie Posters will take a time."</h4>''',
                    unsafe_allow_html=True)
        if dec == 'No':
            pass
        else:
            if sel_gen:
                imdb_score = st.slider('Choose IMDb score:', 1, 10, 8)
                no_of_reco = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(imdb_score)
                table = KNN_Movie_Recommender(test_point, no_of_reco)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                streamlit_style = """
                                                 			<style>
                                                            @import url('https://fonts.googleapis.com/css2?family=PT+Serif&display=swap');
                                                 			html, body, [class*="css"]  {
                                                 			# font-family: 'Roboto', sans-serif;
                                                 			font-family: 'PT Serif', serif;

                                                 			}
                                                 			</style>
                                                 			"""
                st.markdown(streamlit_style, unsafe_allow_html=True)

                i = 0;
                for movie, link, ratings in table:
                    c += 1
                    if i % 2 == 0:
                        # print(link)
                        cols1, cols2 = st.columns(2)
                        with cols1:
                            movie_poster_fetcher(link)

                        with cols2:
                            director, cast, story, total_rat = get_movie_info(link)

                            st.title(movie)
                            st.write(director)
                            st.write(cast)
                            st.write(story)
                            # st.markdown(total_rat)
                            st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
                            st.write(f"(imdb link)[ {movie}]({link})")
                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                    else:
                        cols1, cols2 = st.columns(2)
                        with cols1:
                            director, cast, story, total_rat = get_movie_info(link)
                            st.title(movie)
                            st.write(director)
                            st.write(cast)
                            st.write(story)
                            # st.markdown(total_rat)
                            st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
                            st.write(f"(imdb link)[ {movie}]({link})")

                        with cols2:

                            movie_poster_fetcher(link)

                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                        st.write("\n")
                        st.write(" \n")
                        st.write("  \n")
                    i += 1




run()

