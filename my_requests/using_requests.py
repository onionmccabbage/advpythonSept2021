import requests
import sys

# Access the end-point API at http://jsonplaceholder.typicode.com/
# pass parameters for category and id either as sys arguments (argv) or user input
# grab the returned JSON (or handle exceptions)
# if it's a user, display lat/lon

def getInfo(category='users', id=1): # (optionally) provide sensible defaults
    url = 'http://jsonplaceholder.typicode.com/{}/{}'.format(category, id)
    try:
        response = requests.get(url)
        # .json() takes the returned json text and converts to a dict
        d = response.json() # in this case, we expect JSON
        # also - we could use response.text(), response.html(), response.xml()
        if category == 'users':
            # find lat and lon
            lat = d['address']['geo']['lat']# bracket notation since its a dict
            lon = d['address']['geo']['lng']
            print('User is located at lat:{} Lon:{}'.format(lat, lon))
        else:
            # just print the JSON
            print(d) # prints as a dict
    except Exception as err:
        print('Something went wrong: {}'.format(err))


if __name__ == '__main__':
    # if there were no sys arguments, ask user for parameters
    if len(sys.argv) > 1:
        category = sys.argv[1] # users, posts, albums, photos, todos
        id = sys.argv[2] # 1, 2, 3...
    else:
        category = input('Which category?')
        id = int(float(input('Which id?'))) # every input is a string value

    getInfo(category, id)