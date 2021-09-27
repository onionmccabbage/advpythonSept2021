# we can declare our own custom decorators
def show_args(func): # NB here we pass a function in as a parameter
    # remember - functions are just objects
    def new_func(*args, **kwargs): # NB *args and **kwargs are built in to Python
        print('Running function {}'.format(func.__name__))
        print('Positional arguments: {}'.format(args)) # positional args are ALWAS a tuple
        print('Keyword arguments: {}'.format(kwargs))  # keyword args are ALWAYS a dict
        return func(*args, **kwargs)
    return new_func

def show_intrinsics(func):
    # reveal some of the instrinsics for the function
    def inner_func(*args, **kwargs): # NB *args and **kwargs are built in to Python
        print('Function name is {}'.format(func.__name__))
        print('Docstring is {}'.format(func.__doc__))
        print('in module {}'.format(func.__module__))
        return func(*args, **kwargs)
    return inner_func

# here are some simple methods
# @show_args # this will automatically run our function, passing in the decorated function
def add_ints(a, b):
    # take two integers and return the sum
    # first we check they are int
    if isinstance(a, int) and type(b) == int:
        # all good, add them together
        return a+b
    else:
        return 'fail'

if __name__ == '__main__':
    # exercise our decorator
    x = 1
    y = 2
    print(add_ints(x, y)) # these arguments are positional
    print(add_ints(a=3, b=4)) # these areguments are keyword-value
