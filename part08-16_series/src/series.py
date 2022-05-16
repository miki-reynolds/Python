
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = []

    def rate(self, rating: int):
        self.rating.append(rating)
    
    def average(self):
        if len(self.rating) > 0:
            self.average = sum(self.rating)/len(self.rating)
        return self.average


    def __str__(self):
        genres_str = ", ".join(self.genres)

        if len(self.rating) == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genres_str}\nno ratings"
        
        else:
            ave = sum(self.rating)/len(self.rating)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genres_str}\n{len(self.rating)} ratings, average {ave:.1f} points"


def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        if series.average() > rating:
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result







