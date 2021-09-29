import socket # this lets us open a socket serer for listening to requests

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
        # send a response back to the client
        client.send( buf.upper() ) # here we choose to send the request back as upper case
        # we need a way to quit the server
        if buf == b'quit': # we expect the byte string 'quit'
            print('server is closing')
            server.close()
            break # break out of hte while loop


if __name__ == '__main__':
    myServer()