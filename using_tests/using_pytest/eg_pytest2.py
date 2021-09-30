# invoke pytest as follows:
# python -m pytest eg_pytest2.py

# check a named_tuple is being used as intended

from collections import namedtuple

task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# we can set defaults in case bits are missing
task.__new__.__defaults__ = (None, None, False, None)

# write tests to check it works as intended
def test_default():
    '''Using no parameters should invoke the defaults'''
    t1 = task()
    t2 = task(None, None, False, None)
    assert t1 == t2 # the defaults should match the values provided

def test_member_access():
    '''Check we can acces members of the task using dot notation'''
    t3 = task('Learn Python', 'Agnes')
    assert t3.summary == 'Learn Python'
    assert t3.owner   == 'Agnes'
    assert (t3.done, t3.id) == (False, None)

if __name__ == '__main__':
    t1 = task() # uses defaults
    t2 = task('Learn Python', 'Ethel')
