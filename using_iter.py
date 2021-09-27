# __iter__ is built in to python
# it lets us iterate 

l = [1, 7, 11, 42]

l_iter = iter(l) # we now have an iterable for our list

print(l_iter)
print(l_iter.__next__() ) # yield 1
print(l_iter.__next__() ) # yield 7
print(l_iter.__next__() ) # yield 11

# can we directly acccess __next__ on a list??
# print(l.__next__() ) # nope - list has no yield!!

# iter has built in reverse capabilities
r = reversed(l)

print(r.__next__() ) # 42
for i in r:
    print(i)
