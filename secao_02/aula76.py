"""
Closure
"""

def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet

morning = create_greeting('Good Morning')
evening = create_greeting('Good Evening')

for name in ['Mary', 'John', 'Joseph', 'Richard']:
    print(morning(name))
    print(evening(name))