# here we explore named tuple, zip, deque etc.
from collections import namedtuple

# a normal tuple
t = (True,)

# a named tuple
Duck = namedtuple('Duck', 'bill tail')

d1 = Duck('long', 'short') # long bill, short tail
d2 = Duck('wide', 'short')
d3 = Duck('short', 'long')
d5 = d1._replace(tail='medium', bill='orange') # we cannot mutate the orignal tuple
print(d5.bill)

build = {'bill':'orange', 'tail':'waggly'} # a dict
d4 = Duck(**build) # ** will unpack the members of the dict
print(d4)

# Python also has a feature called 'zip' - nothing to do with compression
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
fruits = ['banana', 'orange', 'kiwi', 'durian']
drink = ('coffee', 'tea', 'water', 'milk')
after = ['tiramasu', 'ice cream', 'pie', 'creme caramel']

j = zip(days, fruits, drink, after)
# iterate over the collection j
for d, f, dr, a in j:
    print('On {} I ate {} with {} then {}'.format(d, f, dr, a))
