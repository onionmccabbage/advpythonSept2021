class Duck(): # all classes ultimately descend from the Object type
    # our class can have properties
    count = 0
    # our class can have methods
    def how_many(cls):
        print('Duck class has {} instances'.format(cls.count))
    # usually classes have an __init__ method
    def __init__(self, name): # we MUST provide self, we MAY provide other parameters
        self.__name = name # this is name mangling - makes it very hard to access the property
        Duck.count += 1 # increment the count
    def __str__(self): # here we override the built in __str__ method (used by print)
        return 'This is a Duck called {}'.format(self.__name)
    # we often use getter and setter methods to access and mutate properties
    # @property # this is called decorator syntax
    def name(self):
        return self.__name
    # @name.setter
    def name(self, new_name):
        # we should check the value is within bounds
        self.__name = new_name

if __name__ == '__main__':
    d = Duck('Howard') # we now have an instance of our Duck class
    e = Duck('Ada') 
    e.__name = 'changed' # this adds an ARBITRARY property to our instance - it is NOT the _name
    # print(e.__name) # we CANNOT easily access mangled property names
    print(e) # calls the __str__ method
    print(d.count)
    e.how_many()
    # we can access and mutate the name via the methods
    e.name = 'Ethel'
    print(e.name)
    print(e)

    # it is possible to access name-mangled members
    print(e._Duck__name)