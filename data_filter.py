import pandas as pd
import time
import unique_algorithm
from posterFind import posterPathFind
from fuzzywuzzy import fuzz

def data_process():

    df = pd.read_csv('movie_preprocessing.csv',low_memory=False)
    def change_value(value):
        return str(value).replace(' ','_')

    df['genres'] = df['genres'].apply(change_value)
    df['original_language'] = df['original_language'].apply(change_value)
    df['production_companies'] = df['production_companies'].apply(change_value)
    df['production_countries'] =df['production_countries'].apply(change_value)

    return df

def extract_tags_and_keywords(input_string):
    tags = []
    keywords = []

    words = input_string.split()

    for word in words:
        if word.startswith('+'):
            tags.append(word[1:])
        else:
            keywords.append(word)
    return [tags,keywords]



def title_search(dataframe, keyword):
    filtered_df = dataframe[dataframe['title'].str.contains("|".join(keyword), case=False, na=False) | dataframe['original_title'].str.contains("|".join(keyword), case=False, na=False)]
    return filtered_df


def tag_search(dataframe, tags, genres_tags, language_tags, production_countries_tags, production_companies_tags):
    if len(tags) == 0:
        return dataframe
    for tag in tags:
        tag = tag.lower()
        if tag == "+adult":
            dataframe = dataframe[dataframe['adult'].str.contains("TRUE", case=False, na=False)]
        elif tag in genres_tags:
            dataframe = dataframe[dataframe['genres'].str.contains(tag, case=False, na=False)]
        elif tag in language_tags:
            dataframe = dataframe[dataframe['original_language'].str.contains(tag, case=False, na=False)]
        elif tag in production_countries_tags:
            dataframe = dataframe[dataframe['production_countries'].str.contains(tag, case=False, na=False)]
        elif tag in production_companies_tags:
            dataframe = dataframe[dataframe['production_companies'].str.contains(tag, case=False, na=False)]
        # elif tag in collection_tags:
        #     dataframe = dataframe[dataframe['belongs_to_collection'].str.contains(tag, case=False, na=False)]
        else:
            return pd.DataFrame(columns=dataframe.columns)
    return dataframe


def DataFilter(User_input):
    df = data_process()
    genres_tags = unique_algorithm.unique_genres_read
    language_tags = unique_algorithm.unique_language_read
    production_companies_tags = unique_algorithm.unique_production_companies_read
    production_countries_tags = unique_algorithm.unique_production_countries_read
    # collection_tags = unique_algorithm.unique_collection
    keyword = extract_tags_and_keywords(User_input)[1]
    tags = extract_tags_and_keywords(User_input)[0]
    Movie_list = title_search(df, keyword)
    Movie_list = tag_search(Movie_list, tags, genres_tags, language_tags, production_countries_tags, production_companies_tags)
    # Movie_list['poster_path'] = Movie_list['imdb_id'].apply(posterPathFind)
   
    return Movie_list


# start_time = time.time()


# result = DataFilter("bat man +animation")
# print(result["genres"])

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")

