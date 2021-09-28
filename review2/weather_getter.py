import requests

class WeatherGetter:
    def __init__(self, city='plymouth', country='uk'):
        # super().__init__()
        self.city    = city
        self.country = country
        self.APIkey  = 'APPID=48f2d5e18b0d2bc50519b58cce6409f1'

    def getWeather(self):
        url_str = 'http://api.openweathermap.org/data/2.5/weather?q={0},{2}&units=metric&{2}'
        url = url_str.format(self.city, self.country, self.APIkey)
        response = requests.get(url)
        # if we are sure it is json we can use response.json()
        data  = response.json() # or response.text then json.dumps()
        if 'main' in data:
            # self.temperature = data['main']['temp']
            return data  

if __name__ == '__main__':
    pass