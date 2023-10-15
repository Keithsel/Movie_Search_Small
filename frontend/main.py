from nicegui import ui
import os
import json

# Load the genre list from the JSON file
genre_list = 'genre.json'
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, genre_list)
with open(file_path, mode ='r') as f:
    genres = json.load(f)

# Create a text input for the search bar
search_term = ui.input(placeholder='Search for a movie')

# Create a button to trigger the search when clicked
ui.button('Search', on_click=lambda: search_movies(search_term.value))

# Create a collapsible panel for the genre filter
with ui.select(genre for genre in genres):
    pass

# Define the function to handle the search
def search_movies(query):
    # Call your search algorithm with the query
    # results = search_algorithm(query)

    # Display the results
    # for result in results:
    #     ui.markdown(result)
    pass

# Define the function to handle genre changes
def handle_genre_change(checked, genre):
    if checked:
        return '+' + genre
    else:
        return '-' + genre

# Run the application
ui.run()
