# Useful dictionary methods in Python
# len - how many keys
# keys - iterable with keys
# values - iterable with values
# items - iterable with keys and values
# setdefault - adds value if key does not exist
# copy - returns a shallow copy (shallow copy)
# get - get a key
# pop - Deletes an item with the specified key (del)
# popitem - Deletes the last added item
# update - Updates one dictionary with another
import copy

d1 = {
    'k1': 1,
    'k2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.deepcopy(d1)

d2['k1'] = 1000
d2['l1'] [1] = 999

print(d1)
print(d2)

