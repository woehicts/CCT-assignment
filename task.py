"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.

Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.

Example:

number_of_cities == 3
cities_with_train_station == [1]

There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.

"""

from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    """Finds the largest possible distance to the nearest train station within a list of cities, using the provided list of the train stations assigned to them.
        
        `number_of_cities` (int) - defines the number of cities within the list
        `cities_with_train_station` (List[int]) - specifies the cities that have the train stations
    """
    if number_of_cities <= 0:
        raise ValueError("The number of cities should not be less than one")
    if not isinstance(cities_with_train_station, list):
        raise TypeError("'cities_with_train_station' should be a list of numbers")
    sorted_stations = sorted(set([city for city in cities_with_train_station if isinstance(city,int) and city >= 0 and city < number_of_cities]))
    number_of_stations = len(sorted_stations)
    if  number_of_stations == 0:
        raise ValueError("Either the train stations haven't been assigned with valid city numbers or the list of stations was an empty list")
    elif number_of_stations == 1:
        max_interstation_half_distance = 0
    else:
        max_interstation_half_distance = max([(station2 - station1)// 2 for station1, station2 in zip(sorted_stations[:-1],sorted_stations[1:])])
    first_station = sorted_stations[0]
    last_station = sorted_stations[-1]
    last_city = number_of_cities - 1
    return max(first_station, last_city - last_station, max_interstation_half_distance)


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")
