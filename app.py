import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de películas
movies = []

# Agregar pelicula
@app.route("/api/new-movie", methods=["POST"])
def new_movie():
    movie_data = json.loads(request.data)
    movie_id = movie_data["movieId"]
    movie_name = movie_data["name"]
    movie_genre = movie_data["genre"]

    movies.append({
        "movieId": movie_id,
        "name": movie_name,
        "genre": movie_genre
    })

    return jsonify({"message": "Película agregada con éxito"})

# ves listado de peliculas por genero
@app.route("/api/all-movies-by-genre/<genre>", methods=["GET"])
def all_movies_by_genre(genre):

    movies_by_genre = [movie for movie in movies if movie["genre"] == genre]

    return jsonify(movies_by_genre)

@app.route("/api/update-movie", methods=["PUT"])
def update_movie():
    movie_data = json.loads(request.data)
    movie_id = movie_data["movieId"]
    movie_name = movie_data["name"]
    movie_genre = movie_data["genre"]

    for movie in movies:
        if movie["movieId"] == movie_id:
            movie["name"] = movie_name
            movie["genre"] = movie_genre
            break

    return jsonify({"message": "Película actualizada con éxito"})

if __name__ == "__main__":
    app.run(debug=True)
