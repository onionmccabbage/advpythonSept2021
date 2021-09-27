# we will access an API end-point to grab a load of JSON data
# we will then expose this data via a custom generator

# may need to install it:  python -m pip install requests
import requests # this gives access to HTTP API end-points

def user_range(first=1, last=10):
    number = first
    while number <= last:
        res = requests.get('http://jsonplaceholder.typicode.com/users/{}'.format(number))
        yield res.text # NB the requests will be made ONLY when yield is invoked
        number += 1

if __name__ == '__main__':
    users = user_range(2, 7)
    for user in users: # invoke yield iteratively
        print(user)

    # grab individuals on demand
    others = user_range(1, 5)
    print(others.__next__() ) # yield member 1
    print(others.__next__() ) # yield member 2
    print(others.__next__() ) # yield member 3
    print(others.__next__() ) # yield member 4

