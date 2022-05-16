def sort_by_seasons(items: list):
    def order_by_seasons(movies):
        return movies["seasons"]
    return sorted(items, key=order_by_seasons)