import pandas as pd
import streamlit as st
import pickle
import bz2
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=bz2.BZ2File("similarity1.pkl",'rb')
newdata=pickle.load(similarity)
movies=pd.DataFrame(movie_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = newdata[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')
Selected_movie_name = st.selectbox(
'Type your Favaurite Movie',
movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(Selected_movie_name)
    for i in recommendations:
        st.write(i)
