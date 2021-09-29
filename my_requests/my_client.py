import sys
import socket
import sys

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    # try to connect to our server
    sock.connect(param_t)
    # send a message to the server
    if len(sys.argv) > 1:
        # take the first and subsequent system arguments and join them with a space between
        msg = ' '.join(sys.argv[1:])
    else:
        msg = 'default message'
    sock.send(msg.encode()) # use the default URL encoding
    # handle any response from the server
    res = sock.recv(1024) # read the first 1024 bytes
    print(res)
    # clean up when done
    sock.close()


if __name__ == '__main__':
    myClient()
