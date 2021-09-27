# recently functional programming has returned in fashion
# a pure function has no side effects 
# i.e. for given inputs the output is entirely predictable
# we need the 'reduce' capabilites of the functools library
from functools import reduce

def square(x):
    return x*x

def add(x,y): # we will use this to recursively 'reduce' a bunch of numbers
    return x+y

# in order to use 'filter' we must return True or False
def isOdd(x): # assume it's an int
    return x%2 != 0 # this function returns True or False

if __name__ == '__main__':
    # here we can exercise this module
    # let's make a list of square numbers
    sq_l= list( map( square, range(1,6) ) ) # take the 'square' fn and apply a bunch of numbers to it
    print(sq_l)
    # we can use a function to filter values
    odds_l = list( filter( isOdd, range(-10**1000, 10**1000) ) )
    # print(odds_l)
    # using 'reduce'
    r = reduce( add, odds_l, 10 ) # also add ten!!
    print(r)
