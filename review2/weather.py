import time
import json
from weather_getter import WeatherGetter
from location_generator import locationGen

def main(city, country):
    start = time.time()
    weatherGetter = WeatherGetter(city, country)
    weather = weatherGetter.getWeather()
    d = weather['weather'][0]['description']
    t = weather['main']['temp']
    n = weather['name']
    ws = weather['wind']['speed']
    wd = weather['wind']['deg']
    report_string = '''Description: {} Temperature: {:.0f}°C in {}
The wind speed is {} coming from {}° 
'''.format(d, t, n, ws, wd)
    print(report_string)
    end = time.time()
    print("Weather received in {} seconds".format(end-start))
    # persist in text file
    with open("reports.txt", 'a') as r:
        for line in report_string:
            r.write(line)

def askUser():
    city = input('Choose a city:')
    # check it's a non empty string, else default
    if type(city)!=str or city =='':
        city='Athlone'
    country = input('choose a country:')
    # check it is 2 or 3 characters in a string else default
    if type(country)!=str or  1>len(country)>4:
        country='ie'
    main(city, country)

def readCities():
    with open('cities.txt', 'rt') as fin:
        locations = fin.readlines()
    # iterate over the locations
    for location in locations:
        city, country = location.split(',')
        # remove the trailing new-line character
        country = country.strip() # or country[:-1]
        main(city, country)

def useLocationGenerator():
    inst = locationGen()
    city, country =  inst.__next__()
    main(city, country)
    city, country =  inst.__next__()
    main(city, country)

if __name__ == '__main__':
    askUser()
    useLocationGenerator()
    readCities()