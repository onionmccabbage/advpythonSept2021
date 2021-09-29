import doctest
def nthPower(d,p):
    '''
    This returns a number raised to a power
    >>> nthPower(-3,2)
    9
    '''
    return d**p

def cubeIt(a,b):
    '''
    return the cube of all numbers in range a to b
    >>> cubeIt(1,3)
    [1, 8, 27]
    >>> cubeIt(1,10) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b+1):
        answers.append(i*i*i)
    return answers

if __name__ == '__main__':
    # print(nthPower(2,3)) # expect 8
    doctest.testmod(verbose=True) # run any doc string tests