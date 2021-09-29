import requests
import sys
import json

def getInfo(category='users', id=1):
    url = 'http://jsonplaceholder.typicode.com/{}/{}'.format(category, id)
    print('The service URL is {}'.format(url))
    try:
        response = requests.get(url)
        d = response.json()
        if category == 'users':
            # find lat and lon
            lat = d['address']['geo']['lat']# bracket notation since its a dict
            lon = d['address']['geo']['lng']
            return 'User is located at lat:{} Lon:{}'.format(lat, lon)
        else:
            # just print the JSON
            return json.dumps(d)
    except Exception as err:
        return 'Something went wrong: {}'.format(err)

if __name__ == '__main__':
    # if there were no sys arguments, ask user for parameters
    if len(sys.argv) > 1:
        category = sys.argv[1] # users, posts, albums, photos, todos
        id = sys.argv[2] # 1, 2, 3...
    else:
        category = input('Which category?')
        id = int(float(input('Which id?'))) # every input is a string value

    getInfo(category, id)