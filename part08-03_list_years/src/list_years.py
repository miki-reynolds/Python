from datetime import date

def list_years(dates: list):
    years = []
    for item in dates:
        years.append(item.year)
    return sorted(years)

