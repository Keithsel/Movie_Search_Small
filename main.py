import streamlit as st
import data.dataProcessing as dp

def genre_filter():
    with st.expander('Genre', expanded=True):
        selected_genres = st.multiselect("Select Genre(s):", dp.unique_genres)

    return [f"+{genre}" for genre in selected_genres]

def languages_filter():
    with st.expander('Language', expanded=True):
        selected_languages = st.multiselect("Select Language(s):", dp.unique_languages)

    return [f"+{language}" for language in selected_languages]

def companies_filter():
    with st.expander('Company', expanded=True):
        selected_companies = st.multiselect("Select Company(s):", dp.unique_production_companies)

    return [f"+{company}" for company in selected_companies]

def main():
    st.title("Movie Search Engine")

    # Keyword search bar
    keyword = st.text_input("Enter movie name or keyword:")

    # Tags
    genres = genre_filter()
    languages = languages_filter()
    companies = companies_filter()

    # Year filter
    # year_start, year_end = st.slider("Select Year Range:", min_value=1900, max_value=2023, value=(1900, 2023), step=1)

    # User rating filter
    user_rating = st.slider("Select User Rating:", min_value=0.0, max_value=10.0, value=(0.0, 10.0), step=0.1)

    # Search Button
    if st.button("Search"):
        st.write(f"Keyword: {keyword}")
        tag_str = ""
        if len(genres) > 0:
            tag_str += f"{', '.join(genres)}, "
        if len(languages) > 0:
            tag_str += f"{', '.join(languages)}, "
        if len(companies) > 0:
            tag_str += f"{', '.join(companies)}, "
        tag_str += f"{user_rating}"
        st.write(f"Tags: {tag_str}")

main()
