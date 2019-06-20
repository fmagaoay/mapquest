## ICS 32 Project 3: Ride Accross The River ##
## Fely Magaoay 27278238 ##
## Module 1: URLs

import json
import urllib.parse
import urllib.request

API_KEY = 'NNZDz3AFCHchdxvZdgAUP8CJzVXw5Agg'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'

def mapquest_url(locations: list) -> str:
    '''This function takes a number of locations (at least 2 )
    and the names of locations, and returns a URL that can be used to ask
    MapQuest Data API for information about the locations'''
    query_parameters = [
        ('key', API_KEY), ('from', locations[0])
    ]
    
    for i in locations[1:]:
        query_parameters.append(('to', i))
        
    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json_result':
    '''This function takes a URL and returns a Python object representing
    the parsed JSON response'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        json_object = json.loads(json_text)
        return json_object

    except:
        print('\n' + 'NO ROUTE FOUND')
        
    finally:
        if response != None:
            response.close()

def latlong_list(json_result):
    '''This function returns a list of latlongs to be used for elevation urls'''
    try:
        latlongs = []
        for item in json_result['route']['locations']:
            latlongs.append((item['latLng']['lat'], item['latLng']['lng']))

    except:
        print('\n' + 'NO ROUTE FOUND')
        
    return latlongs
        
def elevation_url(latlongs):
    '''This functions takes a list of latlongs and returns a list of elevation urls'''
    url_list = []

    for latlong in latlongs:
        elevation_parameters = [
        ('key', API_KEY), 
    ]
        elevation_url = ELEVATION_URL + '/profile?' + urllib.parse.urlencode(elevation_parameters) + '&latLngCollection='+ str(latlong[0]) + ',' + str(latlong[1])
        url_list.append(elevation_url)

    return url_list
