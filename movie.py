import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def index_from_title(title):
    title_list = df['title'].tolist()
    titlesim = difflib.get_close_matches(title, title_list, 1)[0]
    return df[df.title == titlesim]["index"].values[0]

def title_from_index(index):
    return df[df.index == index]["title"].values[0]

df = pd.read_csv('moviedata.csv')
features = ['genres', 'cast', 'director', 'tagline', 'keywords',]
for feature in features:
    df[feature] = df[feature].fillna("")

def combine_features(row):
    try:
        return row['genres'] + " " + row['cast'] + " " + row['director'] + " " + row['tagline'] + " " + row['keywords']
    except:
        print("Error: ", row)

def combine_features(column):
    try:
        return column['genres'] + " " + column['cast'] + " " + column['director'] + " " + column['tagline'] + " " + column['keywords']
    except:
        print("Error:" ,column)

df["combined_features"] = df.apply(combine_features, axis = 1)
user_movie = input("enter your favourite movie")
user_movie_index = index_from_title(user_movie)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)
similar_movies = list(enumerate(cosine_sim[user_movie_index]))
similar_movies_sorted = sorted(similar_movies, key = lambda x:x[1], reverse = True)

i = 0
for element in similar_movies_sorted:
    print (title_from_index(element[0]))
    i += 1
    if i > 25:
        print("here you can see the similar movie")
        break
