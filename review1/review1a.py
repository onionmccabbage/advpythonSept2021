from using_decorators import show_args

@show_args
def mapRoots(start, number):
    '''
    Return the square root of integers between min and max
    '''
    print('Using Map')
    roots = map(lambda x: x**0.5, range(start,number+1))
    for root in roots:
        print (root)

def compRoots(start, number):
    print('Using List comprehension')
    roots = [x**0.5 for x in range(start,number+1)]
    for root in roots:
        print (root)

def genRoots(start, number):
    print('Using Generator comprehension')
    roots = (x**0.5 for x in range(start,number+1))
    for root in roots:
        print (root)

if __name__ == '__main__':
    # number = int(input('Enter number : '))
    start = 0
    number = 12
    mapRoots(start, number)
    compRoots(start, number)
    genRoots(start, number)
