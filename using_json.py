# json is javascript object notation - it is TEXT
import json
import datetime

# here is a rather complex data structure
# in this case a list of dictionaries containing string, numeric, dict and list data
a = [{'name':'PC', 'cost':500, 'detail':{'a':'True', 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':'False', 'b':[9,8,7,6]}}]

# we can convert to json (i.e. to text)
a_j = json.dumps(a) # take the structure and render it as plain text

print(type(a_j), a_j)

# convert back to a structure
b = json.loads(a_j)
print(type(b), b)

# can JSON handle date-time objects? NO
now = datetime.datetime.utcnow()
# now_j = json.dumps(now) # fails
# print(now_j)

# When JSON fails, use pickle
import pickle
p = pickle.dumps(now)
print(now, type(now), p, type(p))
# return to the original structure
n = pickle.loads(p)
print(n, type(n))