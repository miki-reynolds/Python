def read_data(filename: str):
    list = []
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            list.append(parts)
    return list

def get_station_data(filename: str):
    list = read_data(filename)
    stations_coordinates = {}
    for station in list:
        stations_coordinates[station[3]] = (float(station[0]), float(station[1]))
    return stations_coordinates


def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 =stations[station2][1]

    import math 
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    biggest = 0
    smallest = 0

    for station, coordinates in stations.items():
        biggest_difference = coordinates[0] - coordinates[1]
        if biggest_difference > biggest:
            biggest = biggest_difference
            biggest_station = coordinates
            station1 = station

        smallest_difference = coordinates[0] - coordinates[1]
        if smallest == 0 or smallest_difference < smallest:
            smallest = smallest_difference
            smallest_station = coordinates
            station2 = station
            
    # max_long = max(long) - min(long)
    # max_lat = max(lat) - min(lat)

    # import math 
    # x_km = (longitude1 - longitude2) * 55.26
    # y_km = (latitude1 - latitude2) * 111.2
    # distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return station1
    # station1, station2, 


stations = get_station_data('stations1.csv')
# print(stations)
print(greatest_distance(stations))
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
