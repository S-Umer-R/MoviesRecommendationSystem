import streamlit as st
import pickle
import pandas as pd
import requests


page_by_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #2234ae;
background-image: linear-gradient(315deg, #2234ae 0%, #191714 74%);
}
</style>
"""
st.markdown(page_by_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Movie Recommender System</h1>", unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f71289b8cd2ae02f6667f407a4294f03".format(movie_id)
    data = requests.get(url)
    data = data.json()

    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    print(full_path)
    return full_path


movies = pickle.load(open('movie_dict.pkl','rb'))
df = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:7] # enumerate will assign the index number to shortest angle/distance, reverse is used for descending order
    
    rec_movies = []
    rec_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id  # Access 'movie_id' directly from the dictionary
        rec_movies.append(df.iloc[i[0]].title)
        rec_poster.append(fetch_poster(movie_id))

    return rec_movies, rec_poster

option = st.selectbox(
    'Enter the movie name',
    df['title'].values)

if st.button('Select'):
    my_movie_id = df.loc[df['title'] == option, 'movie_id'].values[0]
    st.write("Your Movie:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.text(option)
        st.image(fetch_poster(my_movie_id), width=200)

    with col3:
        st.write(' ')
    


    st.write('Similar Movies:')
    movie_names,movie_posters = recommend(option)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
    with col6:
        st.text(movie_names[5])
        st.image(movie_posters[5])
