from threading import Thread # this is a Thread access object
import time
import random
import sys

# create a runnable class (descends from the Thread class)
class MyClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name 
    # override the 'run' method of the Thread class
    def run(self): # this gets called every time we start an instante this class
        # do something that takes some time
        for i in range(1, 50):
            time.sleep(random.random()*0.1)
            sys.stdout.write(self.name) # or print()

if __name__ == '__main__':
    # some instances of our class
    m1 = MyClass('m1')
    m2 = MyClass('m2')
    m3 = MyClass('m3')
    m4 = MyClass('m4')
    # start the threads
    m1.start() # calls the run method
    m2.start()
    m3.start()
    m4.start()
    # rejoin the threads to the main thread
    m1.join()
    m2.join()
    m3.join()
    m4.join()