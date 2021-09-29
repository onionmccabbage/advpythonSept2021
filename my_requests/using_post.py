import requests # lets us make 'get' or 'post' requests

# to make a POST request, we pass a 'payload' of data

def makePost():
    url = 'https://httpbin.org/post' # an echo API end point service
    payload = {'item':'monitor', 'price':'200'} # dict
    try:
        r = requests.post(url, data=payload )
        print(r.text)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makePost()