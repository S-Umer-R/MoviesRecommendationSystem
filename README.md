# Movie Recommender System

## Introduction

This project aims to develop a movie recommendation system using both content-based and user-based collaborative filtering. The dataset used is from TMDB, containing movie details such as title, overview, genres, keywords, cast, and crew. The implementation is in Python, utilizing libraries like NumPy, Pandas, Scikit-learn, Matplotlib, and SpaCy.

## Visualizations

The code includes visualizations showcasing various movie statistics. Bar plots display the top 10 movies based on vote average, popularity, budget, and revenue. Another plot shows the top 5 languages based on the number of movies produced.

## Content-Based Recommendation System

### 1. Data Preprocessing
- Merged movies and credits data frames based on movie title.
- Extracted relevant features, removed movies with missing overviews, and converted string representations to lists.
- Extracted top 3 cast members and directors.

### 2. Feature Engineering
- Concatenated relevant features into a 'tags' column.
- Cleaned and lemmatized tags using SpaCy for better vectorization.

### 3. TF-IDF Vectorization
- Used TF-IDF vectorization to convert tags into numerical vectors.
- Selected the top 5000 features to represent the movies.

### 4. Cosine Similarity
- Calculated cosine similarity between movie vectors.
- Implemented a recommendation function suggesting five movies similar to a given movie.

## User-Based Collaborative Filtering

### 1. Top 100 Movies Selection
- Sorted movies based on popularity in descending order.
- Selected the top 100 movies.

### 2. Generated User Data
- Created a dataset simulating user-movie interactions for 10 users.
- Assigned random movie ratings to simulate user preferences.

### 3. User-Based Collaborative Filtering
- Built a user-item matrix to represent user-movie interactions.
- Calculated cosine similarity between users.
- Recommended movies to a user based on the preferences of similar users.

## Usage

### Content-Based Recommender System
- Load libraries and the TMDB dataset.
- Preprocess data, implement the movie recommender function using cosine similarity.
- Visualize top 10 movies based on different criteria and top 5 languages.
- Provide a movie title as input to the 'recommend' function to receive movie recommendations.

### User-Based Collaborative Recommender System
- The notebook generates user data and stores it in "new_movie_dataset.csv."
- Find the user-based collaborative filtering section in the notebook.
- Use the `recommend_movies(user_id, num_recommendations)` function:
  - Input the user's ID (e.g., `recommend_movies(100)`).
  - Adjust `num_recommendations` for the desired number of movie recommendations.
- Explore recommendations for different users by changing the user ID (100 to 110).
- Fine-tune parameters or modify the collaborative filtering model as needed.

## Conclusion

The project successfully implemented both content-based and user-based collaborative filtering recommendation systems, providing personalized movie recommendations.

## UI Implementation

In addition to the backend systems, a user interface has been implemented using the Streamlit framework. This interface enhances user experience, allowing users to input preferences, view recommendations, and explore 5000 movies based on popularity.

### Instructions to Run the Movie Recommender UI

1. **Navigate to the Web App Directory:**
   - Open the terminal.
   - Change the directory to the "movie recommender webapp" folder.

2. **Run the Streamlit Web App:**
   - Type the following command in the terminal: `streamlit run webapp.py`.
   - Press Enter to execute the command.

3. **Access the Web App:**
   - Once the command is executed, a local development server will start.
   - Open a web browser and go to the provided URL.
   - Explore the Movie Recommender Web App, input user preferences, and discover movie recommendations.

4. **Interact with the UI:**
   - Use the interactive features provided by the Streamlit interface to engage with the recommendation system.
   - View recommended movies based on preferences and explore the top 100 movies.

Enjoy personalized movie recommendations through the user-friendly web interface!
