## ICS 32 Project 3: Ride Across the River ##
## Fely Magaoay 27278238 ##
## Module 3: User Interface ##

import project3_class
import project3_urls

def run_results(results: ['result']):
    for result in results:
        current_outputs = result.outputs()

    return current_outputs

def location_number(locationnumber):
    locations = []
    for i in range(locationnumber):
        fromlocation = input('')
        locations.append(fromlocation)

    return locations

def list_of_locations(locations):
    url = project3_urls.mapquest_url(locations)            
    json_result = project3_urls.get_result(url)

    return json_result


def list_of_elevationurls(json_result):
    latlongs = project3_urls.latlong_list(json_result)
    
    return latlongs

def elevations(latlongs):
    elevationurl = project3_urls.elevation_url(latlongs)
    dictionary = []
    for url in elevationurl:
        elevation_result = project3_urls.get_result(url)
        dictionary.append(elevation_result)

    return dictionary

def number_of_inputs(outputs):
    inputs = []
    for item in range(outputs):
        info = input('')
        inputs.append(info)
        
    return inputs

def name_of_inputs(outputs, json_result, elevationurls):
    inputs = number_of_inputs(outputs)

    results = []          
    for i in inputs:
        if i == 'LATLONG':
            results.append(project3_class.Latlong(json_result))
        elif i == 'STEPS':
            results.append(project3_class.Steps(json_result))
        elif i== 'TOTALTIME':
            results.append(project3_class.Time(json_result))
        elif i == 'TOTALDISTANCE':
            results.append(project3_class.Distance(json_result))
        else:
            results.append(project3_class.Elevation(elevationurls))

    return results

def user_interface():
    locationnumber = (int(input('')))
    locations = location_number(locationnumber)
    json_result = list_of_locations(locations)

    #elevation urls 
    latlongs = list_of_elevationurls(json_result)  
    elevationurls = elevations(latlongs)
    
    outputs = int(input(''))
    results = name_of_inputs(outputs, json_result, elevationurls)
            
    run_results(results)
    
    print('\n' + 'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
         

if __name__ == '__main__':
    try:
        user_interface()
    except:
        print('\n' + 'MAPQUEST ERROR')
