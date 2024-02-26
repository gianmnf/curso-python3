# Modifying keys and values in dictionaries

person = {}

key = 'full_name'

person[key] = 'Gian'
person['surname'] = 'Michel'

print(person[key])

person[key] = 'Mary'

del person['surname']
print(person)
print(person['full_name'])

if person.get('surname') is None:
    print('Unavailable')
else:
    print(person['surname'])