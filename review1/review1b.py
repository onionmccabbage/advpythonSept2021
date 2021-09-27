from using_decorators import show_args
from using_decorators import show_intrinsics

@show_intrinsics
def is_square(number):
    '''
    determine if a value is a square number
    '''
    if type(number) == int and number > -1:
        root = number**0.5
        check = int(number**0.5)
        return root == check
    else:
        return False 

@show_args
def filterSquares(start, stop):
    '''
    Use the 'is_square' method to filter just square nubmers 
    '''
    numbers_sq = list(filter(is_square, range(start, stop+1)))
    for n in numbers_sq:
        print(n)

if __name__ == '__main__':
    filterSquares(3, 33)
    