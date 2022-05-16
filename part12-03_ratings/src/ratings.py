def sort_by_ratings(items: list):
    def order_by_ratings(movies):
        return movies["rating"]
    return sorted(items,key=order_by_ratings, reverse=True)