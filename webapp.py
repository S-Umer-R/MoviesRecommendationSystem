import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

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

# Function to check if the file exists in the current directory
def file_exists(file_path):
    return os.path.isfile(file_path)

# Function to download the file from the provided URL
def download_file_from_url(url, file_name):
    print("Downloading file...")
    gdown.download(url, output=file_name)
    print("File downloaded successfully!")

# Replace with the provided Google Drive file URL
file_url = "https://drive.google.com/uc?id=1epxvbJA82_ToF9gTFT9TnqoT86ERukNo"

# Replace with your desired file name
file_name = "similarity.pkl"

if file_exists(file_name):
    print("File already exists.")
else:
    download_file_from_url(file_url, file_name)

# Load the pickle file into the 'similarity' variable
with open(file_name, 'rb') as f:
    similarity = pickle.load(f)

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

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:7]
    
    rec_movies = []
    rec_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        rec_movies.append(df.iloc[i[0]].title)
        rec_poster.append(fetch_poster(movie_id))

    return rec_movies, rec_poster

def main():
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
        movie_names, movie_posters = recommend(option)
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

if __name__ == "__main__":
    main()
