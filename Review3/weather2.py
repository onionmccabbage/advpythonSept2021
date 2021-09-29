import json
import sqlite3
import datetime
import requests

conn = sqlite3.connect('weather_db')
curs = conn.cursor()
statement = '''CREATE TABLE weather
                (date DATETIME PRIMARY KEY,
                 city VARCHAR(255),
                 country VARCHAR(3),
                 description VARCHAR(255),
                 temperature FLOAT)'''
curs.execute(statement)
conn.commit()
def gen():
    with open('cities.txt','rt') as f1:
        for line in f1.readlines():
            city, country = line.split(',')
            yield city, country.strip()
for city_inst, country_inst in gen():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'.format(city_inst, country_inst)
    response = requests.get(url) 
    weather = json.loads(response.text) 
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    now = datetime.datetime.utcnow()
    # wspeed = weather['wind']['speed']
    # wdirection = weather['wind']['deg']
    statement = '''INSERT INTO weather VALUES("{}","{}","{}","{}",{})'''.format(now.strftime('%Y-%m-%d %H:%M:%S.%f'),city_inst,country_inst,desc,temp)
    # print(statement)
    curs.execute(statement)
    conn.commit()

statement = '''SELECT * FROM weather'''
curs.execute(statement)
rows = curs.fetchall()
print(rows)
conn.commit()
conn.close()