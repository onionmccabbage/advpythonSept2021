# a good strategy:
# 1. come up with the plan
# 2. write tests (no code yet)
# 3. write code
# 4. STOP when tests pass (reduces feature-bloat)

# we may need to: pip install pytest
# invoke pytest as follows:
# python -m pytest eg_pytest1.py
# we can use pytest for this:

# assert <space> logical_entity <comparator> other_logical_entity

def test_passing():
    assert (1,2,3) == (1,2,3) # same ordinal values, test will pass

# def test_failing():
#     assert (1,2,3) == (3,2,1) # different ordinal values

def test_sets():
    assert {1,2,3} == {3,2,1} # set has no ordinal values