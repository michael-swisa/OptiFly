import math

weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.25,
    "pilot_skill" : 0.25,
    "weather_conditions" : 0.20,
    "execution_time" : 0.10,
    "priority":0.15
}

def haversine_distance(lat1, lon1):
    lat2 = 32.6307267 # Destination latitude
    lon2 = 35.3488686 # Destination longitude
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance
