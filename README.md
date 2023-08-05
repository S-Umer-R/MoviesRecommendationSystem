# Movie Recommender System on the basis of Content-Based Filtering

This is a Python implementation of a movie recommender system based on the TMDB (The Movie Database) dataset. The system uses content-based filtering to recommend movies similar to a given movie. Content-based filtering relies on analyzing the content or features of items to make recommendations.

### Dataset
The TMDB dataset contains information about various movies, including their titles, genres, keywords, cast, crew, budget, revenue, popularity, vote average, and more. The dataset is used to extract essential features for building the movie recommender system.

### Data Preprocessing
Before building the recommender system, the dataset is preprocessed to extract relevant features. The important features include 'movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', and 'crew'. Null values for the 'overview' column are dropped.

The 'genres', 'keywords', 'cast', and 'crew' columns are initially stored as strings in the form of a list of dictionaries. A conversion function is used to extract the names of genres, keywords, cast members, and directors and store them as lists.

The 'overview' column is converted into a list to concatenate it with other features, creating a unified set of tags that represent each movie.

### Data Transformation
The tags representing each movie are then transformed into a string and converted to lowercase. This allows the model to work with a unified and consistent representation of the movie tags.

### Feature Engineering
Next, stemming is performed on the tags to reduce the words to their root form. This process helps in reducing the dimensionality of the data while retaining semantic meaning.

The CountVectorizer is then used to convert the preprocessed tags into a vector representation. This step transforms the textual data into a numerical format, suitable for computing similarities between movies.

### Cosine Similarity
Cosine similarity is utilized to calculate the similarity between movies. Cosine similarity computes the angle between two vectors in a multi-dimensional space. In the context of the movie recommender system, it measures the similarity between the tag vectors representing different movies.

### Recommender Function
The 'recommend' function takes a movie title as input and returns a list of five movies with the highest similarity (lowest angle) to the given movie. It fetches the index of the input movie in the DataFrame, computes the similarity between the input movie and all other movies, and then sorts the movies based on their similarity.

### Visualizations
The code also includes visualizations to showcase various movie statistics. Bar plots are used to display the top 10 movies based on vote average, popularity, budget, and revenue. Additionally, a bar plot shows the top 5 languages based on the number of movies produced in each language.

### Requirements
To run this movie recommender system, you will need the following libraries installed in your Python environment:
- numpy
- pandas
- matplotlib
- scikit-learn
- nltk

The dataset used in this system is the TMDB dataset ('tmdb_5000_movies.csv' and 'tmdb_5000_credits.csv'). Ensure that these datasets are available in the specified file paths.

### Usage
1. Load the required libraries and the TMDB dataset.
2. Preprocess the data to extract essential features and create movie tags.
3. Implement the movie recommender function using cosine similarity.
4. Visualize the top 10 movies based on different criteria (vote average, popularity, budget, and revenue).
5. Visualize the top 5 languages based on the number of movies produced.
6. Provide a movie title as input to the 'recommend' function to receive movie recommendations.

### Note
Please make sure to have a proper understanding of the code and its requirements before executing it. Additionally, you can further optimize or modify the system to suit your specific use case or dataset.

**Disclaimer:** The data used in this recommender system is from the TMDB dataset, and credit for the data goes to TMDB. This system is intended for educational and illustrative purposes only and may not provide the best recommendations for real-world applications.

Demo link: https://moviesrecommendationsystem.streamlit.app/

### Using webapp_user.py to Run Locally

To run the web application locally, use the `webapp_user.py` script. I've created the `webapp.py` script specifically for running on Streamlit, as the `similarity.pkl` file is too large to be uploaded to GitHub. Therefore, I need to access it from Google Drive. However, you won't encounter the same issue with the `webapp_user.py` script, so feel free to use it.
