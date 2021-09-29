import socket # this lets us open a socket serer for listening to requests
from usr_service import getInfo
from weather_service import WeatherGetter

def myServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    # we need to configure our socket
    param_t = ('localhost', 9874)
    server.bind(param_t)
    # begin listening for requests
    server.listen(5) # we can configure the max number of connections
    print('The server is listening on {} port {}'.format(param_t[0], param_t[1]))
    # respond to requests in an endless loop (with a quit option)
    while True:
        # unpack any request
        (client, addr) = server.accept()
        # read data from the client
        buf = client.recv(1024) # in this case we read the first 1024 bits of the request
        print('Server received {}'.format(buf))
        # we need a way to quit the server
        if buf == b'quit': # we expect the byte string 'quit'
            print('server is closing')
            server.close()
            break # break out of the while loop
        # check what the user is asking for
        if buf.find(b'weather/')== 0: # -1 if not found
            w, city, country = buf.split(b'/') # throw away 'w'
            print('requesting weather for {} {}'.format(city, country))
            # make a call for weather data
            w_s = WeatherGetter(city.decode(), country.decode())
            w = w_s.getWeather()
            print('Proxy Service received: {}'.format(w))
            # send the response back to the client
            client.send(w)
        elif buf.find(b'/'):
            cat, id = buf.split(b'/') # we can split bytes just like strings!
            print('requesting data for {} {}'.format(cat, id))
            # make a call for user data
            d = getInfo(cat.decode(), int(id)) # decode bytes to string
            print('Proxy Service received: {}'.format(d))
            # send the response back to the client
            client.send(d.encode())
        else:
            # just send a response back to the client
            client.send( buf.upper() ) # here we choose to send the request back as upper case


if __name__ == '__main__':
    myServer()