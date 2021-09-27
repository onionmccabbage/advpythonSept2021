# we can use comprehensions to comprehensively iterate over a collection
# Custom generators yield custom values to comprehensions

# we can define our OWN generator
def my_range(first=0, last = 10, step=1):
    '''
    return sum for all members in range
    default 0-10 step 1
    '''
    number = first
    while number < last:
        yield number # yield in place of return
        number += number + step

if __name__ == '__main__':
    pass
    # we can iterate comprehensively over ANY collectino
    # e.g. a set (here is a set comprehension)
    s = {number for number in range(-9, 10) if number%3 == 0} # values which are multiples of three
    print(s)
    # we can use our own range geneerator
    r = my_range()
    print(r) # a generator object, since it has a yield statement
    # we can iterate over our custom generator
    for item in r: # this calls the yield
        print(item)

    # once we have exhausted the generator there is nothing left to yield
    # print(r.__next__()) # fail - nothing left to yield

    # custom generators will yield values without persisting them in memory
    t = my_range(99, 10*1000, 5)
    # we can pick the next value whenever we want...
    print(t.__next__() ) # 99
    print(t.__next__() ) # 104+99
    print(t.__next__() ) # 203 + 109
    print(t.__next__() ) # 
    print(t.__next__() ) # 