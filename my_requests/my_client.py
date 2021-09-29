import sys
import socket
import sys

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    # try to connect to our server
    sock.connect(param_t)

if __name__ == '__main__':
    myClient()
