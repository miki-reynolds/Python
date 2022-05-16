def find_movies(database: list, search_term: str):
    new = []
    for movie in database:
        if search_term in movie["name"].lower():
            new.append(movie)
    return new