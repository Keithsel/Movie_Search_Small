import streamlit as st
import json
import data.dataProcessing as dp


def genre_filter():
    selected_genres = []

    with st.expander('Genre', expanded=True):
        col1 = st.columns(1)

        with col1[0]:
            for genre in dp.unique_genres:
                state = st.checkbox(genre, key=genre)

                if state:
                    selected_genres.append(f"+{genre}")

    return selected_genres

def main():
    st.title('Movie Search Engine')

    # Search bar
    keyword = st.text_input("Search for a movie", '')

    # Genre filter
    selected_genres = genre_filter()

    # Display selected filters
    if st.button('Search'):
        st.write('Keyword:', keyword)
        st.write('Selected Genres:', ', '.join(selected_genres))

main()