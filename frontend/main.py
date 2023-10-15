import streamlit as st
import os
import json

# Load the genre list from the JSON file
import json

with open('data/genre.json', 'r') as f:
    genres = json.load(f)

def genre_filter():
    selected_genres = []
    excluded_genres = []

    with st.expander('Genre', expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            for genre in genres[:len(genres)//2]:
                state = st.checkbox(genre, key=genre)

                if state:
                    selected_genres.append(f"+{genre}")

        with col2:
            for genre in genres[len(genres)//2:]:
                state = st.checkbox(genre, key=genre)

                if state:
                    selected_genres.append(f"+{genre}")

    return selected_genres, excluded_genres

def main():
    st.title('Movie Search Engine')

    # Search bar
    keyword = st.text_input("Search for a movie", '')

    # Genre filter
    selected_genres, excluded_genres = genre_filter()

    # Display selected filters
    if st.button('Search'):
        st.write('Keyword:', keyword)
        st.write('Selected Genres:', ', '.join(selected_genres))
        st.write('Excluded Genres:', ', '.join(excluded_genres))

main()