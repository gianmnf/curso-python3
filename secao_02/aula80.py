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

person = {
 'name': 'Gian',
 'surname': 'Michel',
 'age': 18,
}

# print(len(person))

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# print(list(person.items()))

person.setdefault('age', 18)
print(person['age'])