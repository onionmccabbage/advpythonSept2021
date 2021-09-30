# cProfile is a performant way to profile non-trivial code
# invoke cProfile as follows:
# python -m cProfile -o profiling_output using_cProfile.py
# this will record
# number of calls, total times, time per call, cumulative times

from functools import reduce

# the Fibonacci series is a famous mathematical time-waster

def fib1(n): # way more performant - under a second for fib(42)
    sequence = (0,1)
    for _ in range(2, n+1):
        sequence += (reduce(lambda a,b: a+b, sequence[-2:]),)
    return sequence[n]

def fib2(n):
    if n<=1:
        return n
    else:
        return(fib2(n-1)+fib2(n-2)) # call the SAME function iteratively (recursion)

if __name__ == '__main__':
    # print(fib2(42)) # careful - this is demanding of your PC - about 70 sec on my pc
    print(fib1(42)) # is this any faster?
