# in Python 3 there is a context manager
from contextlib import contextmanager
import sys

#this time we will use functional programming
@contextmanager # we decorate our function with the context manager
def stdout_redirect(new_stdout):
    save_stdout = sys.stdout
    sys.stdout = new_stdout
    yield # this will yield the next available object to be written
    # when done, return the original stdout
    sys.stdout = save_stdout

if __name__ == '__main__':
    with open('mylog.txt', 'a') as fobj:
        with stdout_redirect(fobj):
            # we can write multiple lines...
            print('''this is 
redirected 
by our decorated 
method''')
    print('and back to the terminal')