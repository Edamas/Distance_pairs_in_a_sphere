from math import radians, cos, sin, asin, sqrt, pi

# driver code  
lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 =  -1.6997222222222223

def dist(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])  # convert decimal degrees to radians 
    dif_lon, dif_lat = lon2 - lon1, lat2 - lat1  # haversine formula  
    earth_radius_km = 6371.0088 
    earth_circumference_km = 2 * pi * earth_radius_km
    distance_short_km = earth_radius_km * (2 * asin(sqrt(sin(dif_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2) ** 2)))
    distance_long_km = earth_circumference_km - distance_short_km
    return distance_short_km, distance_long_km

distance_short_km, distance_long_km = dist(lat1, lon1, lat2, lon2)
print(f'Short distance: {distance_short_km:18,.4} km')
print(f'Long distance:  {distance_long_km:18,.8} km')

# Source: https://medium.com/analytics-vidhya/finding-nearest-pair-of-latitude-and-longitude-match-using-python-ce50d62af546
# Source: https://tutorialspoint.dev/algorithm/geometric-algorithms/program-distance-two-points-earth
# Earth radius: https://en.wikipedia.org/wiki/Earth_radius

