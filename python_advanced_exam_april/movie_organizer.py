def movie_organizer(*movies):
    genre_counts = {}
    genre_movies = {}

    for movie in movies:
        movie_name, genre = movie
        if genre in genre_counts:
            genre_counts[genre] += 1
            genre_movies[genre].append(movie_name)
        else:
            genre_counts[genre] = 1
            genre_movies[genre] = [movie_name]

    sorted_genres = sorted(genre_counts.keys(), key=lambda x: (-genre_counts[x], x))
    output = []
    for genre in sorted_genres:
        genre_movies[genre].sort()
        genre_output = f"{genre} - {genre_counts[genre]}\n"
        genre_output += "* " + "\n* ".join(genre_movies[genre])
        output.append(genre_output)

    return "\n".join(output)

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy"))
)
