# Load spacy library

import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

#  Function to read the movie.txt file andreturn a list of movie titles and desctiptions

def read_movie_descriptions(file_path):

    movie_data = []
    with open(file_path, "r") as file:
        for line in file:
            title, description = line.strip().split(":")
            movie_data.append((title.strip(), description.strip()))
    return movie_data

# Function to find similar movie based on spacy similarirt score

def find_most_similar_movie(user_description, movie_data):
    
    user_doc = nlp(user_description)
    max_similarity = 0
    most_similar_movie = None

    for title, description in movie_data:
        movie_doc = nlp(description)
        similarity = user_doc.similarity(movie_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = title

    return most_similar_movie

# Read movie descriptions from the file

movies_file_path = "movies.txt"
movie_descriptions = read_movie_descriptions(movies_file_path)

# Example usage

user_description = (
    "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,"
    " the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace."
    " Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
)

recommended_movie = find_most_similar_movie(user_description, movie_descriptions)

print(" ")
print(f"Your Recommended movie is: {recommended_movie}")