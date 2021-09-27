# there are many things built in to Python
# many of these are intrinsic to Python
# they are called intrinsics

class TopLevel():
    def __init__(self):
        pass

class Derived(TopLevel):
    """
    This class is derived from the TopLevel class
    It has it's own __str__ method (used by any 'print' statements)
    """
    def __init__(self):
        super().__init__() # call the init method of the parent class
    def __str__(self):
        return('Derived class instance')

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d) # this will invoke our __str__ method
    # we can explore the instrinsic members of our instances
    print('Class name is: {}'.format(Derived.__name__))
    print('Class doctstring is {} in module {}'.format(Derived.__doc__, Derived.__module__))
    print('The class bases are: {} and dict is: {}'.format(Derived.__bases__, Derived.__dict__))