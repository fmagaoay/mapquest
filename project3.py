## ICS 32 Project 3: Ride Across the River ##
## Fely Magaoay 27278238 ##

import json
import urllib.parse
import urllib.request

API_KEY = 'NNZDz3AFCHchdxvZdgAUP8CJzVXw5Agg'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'
    
class Steps:
    def __init__(self, json_result):
        self.steps = json_result['route']['legs']

    def outputs(self):
        print('\n' + 'DIRECTIONS')
        for item in self.steps:
            for i in item['maneuvers']:
                print (str(i['narrative']))
        
class Distance:
    def __init__(self, json_result):
        self.distance = json_result['route']['distance']
        
    def outputs(self):
        print('\n' + 'TOTAL DISTANCE: ' + str(round(self.distance)) + ' ' + 'miles')
    
class Time:
    def __init__(self, json_result):
        self.time = json_result['route']['time']
    def outputs(self):
        print('\n' + 'TOTAL TIME: ' + str(round(self.time/60)) + ' ' + 'minutes')
        
class Latlong:
    def __init__(self, json_result):
        self.latlong = json_result['route']['locations']
    def outputs(self):
        print('\n' + 'LATLONGS')
        for item in self.latlong:
            if item['latLng']['lat'] > 0 and item['latLng']['lng'] > 0:
                print(str("{0:.2f}".format(item['latLng']['lat'])) + 'N' + ' ' + str("{0:.2f}".format(item['latLng']['lng'])) + 'E')
            elif item['latLng']['lat'] > 0 and item['latLng']['lng'] < 0:
                print(str("{0:.2f}".format(item['latLng']['lat'])) + 'N' + ' ' + str("{0:.2f}".format(abs(item['latLng']['lng']))) + 'W')
            elif item['latLng']['lat'] < 0 and item['latLng']['lng'] > 0:
                print(str("{0:.2f}".format(abs(item['latLng']['lat']))) + 'S' + ' ' + str("{0:.2f}".format(item['latLng']['lng']) + 'E'))
            else:
                print(str("{0:.2f}".format(abs(item['latLng']['lat']))) + 'S' + ' ' + str("{0:.2f}".format(abs(item['latLng']['lng'])) + 'W'))
                
class Elevation:
    def __init__(self, elevation_url: list):
        self.elevation = []
        for elevation in elevation_url:
            self.elevation.append(elevation['elevationProfile'])
    
    def outputs(self):
        print('\n' + 'ELEVATIONS')
        for item in self.elevation:
            print(round(item[0]['height']*3.28084))


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

def _latlong_list(json_result):
    '''This function returns a list of latlongs to be used for elevation urls'''
    try:
        latlongs = []
        for item in json_result['route']['locations']:
            latlongs.append((item['latLng']['lat'], item['latLng']['lng']))

    except:
        print('\n' + 'NO ROUTE FOUND')
        
    return latlongs
        
def _elevation_url(latlongs):
    '''This functions takes a list of latlongs and returns a list of elevation urls'''
    url_list = []

    for latlong in latlongs:
        elevation_parameters = [
        ('key', API_KEY), 
    ]
        elevation_url = ELEVATION_URL + '/profile?' + urllib.parse.urlencode(elevation_parameters) + '&latLngCollection='+ str(latlong[0]) + ',' + str(latlong[1])
        url_list.append(elevation_url)

    return url_list

def run_results(results: []):

    for result in results:
        current_outputs = result.outputs()

    return current_outputs


def user_interface():
    locationnumber = (int(input('')))
    locations = []
    for i in range(locationnumber):
        fromlocation = input('')
        locations.append(fromlocation)
             
    url = mapquest_url(locations)            
    json_result = get_result(url)

    #elevation    
    latlongs = _latlong_list(json_result)
    elevationurl = _elevation_url(latlongs)
    dictionary = []
    for url in elevationurl:
        elevation_result = get_result(url)
        dictionary.append(elevation_result)
        

    outputs = int(input(''))
    inputs = []
    for item in range(outputs):
        info = input('')
        inputs.append(info)

    total_distance = Distance(json_result)
    total_time = Time(json_result)
    latlong = Latlong(json_result)
    steps = Steps(json_result)
    elevation = Elevation(dictionary)

    results = []          
    for i in inputs:
        if i == 'LATLONG':
            results.append(latlong)
        elif i == 'STEPS':
            results.append(steps)
        elif i== 'TOTALTIME':
            results.append(total_time)
        elif i == 'TOTALDISTANCE':
            results.append(total_distance)
        else:
            results.append(elevation)
            
    run_results(results)
    
    print('\n' + 'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
         

if __name__ == '__main__':
    user_interface()
##    try:
##        user_interface()
##    except:
##        print('\n' + 'MAPQUEST ERROR')

