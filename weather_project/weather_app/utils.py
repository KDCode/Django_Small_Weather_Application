import requests

def city_coordinates(city_name):
    # This can be replaced with a more robust method or API to fetch coordinates
    cities = {
        "Delhi": {"latitude": 28.6139, "longitude": 77.2090},
        "New York": {"latitude": 40.7128, "longitude": -74.0060},
        "London": {"latitude": 51.5074, "longitude": -0.1278},
        # Add more cities as needed
    }
    return cities.get(city_name, {"latitude": None, "longitude": None})
