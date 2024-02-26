# Dictionaries in Python (dict type)
# Dictionaries are data structures of the type
# "key" and "value" pair.
# Keys can be considered as the "index"
# that we saw in the list and can be immutable types
# like: str, int, float, bool, tuple, etc.
# Value can be of any type, including other
# dictionary.
# We use the curly braces - {} - or the dict class to create
# dictionaries.
# Immutable: str, int, float, bool, tuple
# Mutable: dict, list
# person = {
# 'name': 'Gian',
# 'surname': 'Michel',
# 'age': 18,
# 'height': 1.8,
#     'Adresses': [
# {'street': 'my street', 'number': 123},
# {'street': 'other street', 'number': 321},
# ]
# }
# person = dict(name='Gian', surname='Michel')

# person = dict(name='Gian', surname='Michel')

person = {
 'name': 'Gian',
 'surname': 'Michel',
 'age': 18,
 'height': 1.8,
 'adresses': [
    {'street': 'my street', 'number': 123},
    {'street': 'other street', 'number': 321},
  ]
}

print(person['name'])
print(person['surname'])

print()

for key in person:
    print(key, person[key])