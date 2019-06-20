# ICS 32 Project 3: Ride Across the River ##
## Fely Magaoay 27278238 ##
## Module 2: Classes ##

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
