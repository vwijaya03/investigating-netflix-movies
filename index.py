# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
# duration = 
filter_duration = (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000) & (netflix_df['type'] == "Movie")

nineties_movies = netflix_df[filter_duration]
nineties_movies['frequent_duration'] = nineties_movies['duration'].astype(str).str.extract('(\d+)')
duration = nineties_movies['duration'].mode().iloc[0]

# print(nineties_movies[['release_year', 'type', 'duration']])
filterActionGenre = (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000) & (netflix_df['type'] == "Movie") & (netflix_df['genre'] == 'Action') & (netflix_df['duration'] < 90)
action_movies = netflix_df[filterActionGenre]
short_movie_count = action_movies[filterActionGenre].shape[0]

print(short_movie_count)