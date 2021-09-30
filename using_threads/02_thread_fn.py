# many threads can run on one processor (using shared inst of Python)
from threading import Thread # this is a Thread access object
import time
import random
import sys

# create a thread-runnable function
def myFunc(name):
    # do something long-tail
    for i in range(1,50):
        time.sleep(random.random()*0.1 ) # 0.1, 0.2, 0.3 etc.
        sys.stdout.write(name) # or print()


# NB all threads run consecutively and independently
if __name__ == '__main__':
    # call our function using several threads
    thr1 = Thread(target=myFunc, args=('thr1',)) # args must be a tuple
    thr2 = Thread(target=myFunc, args=('thr2',)) # args must be a tuple
    thr3 = Thread(target=myFunc, args=('thr3',)) # args must be a tuple
    thr4 = Thread(target=myFunc, args=('thr4',)) # args must be a tuple

    # we need to start any threads
    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()
    # we need to rejoin to the main thread
    thr1.join()
    thr2.join()
    thr3.join()
    thr4.join()