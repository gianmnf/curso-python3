"""
Higher Order Functions
Funções de primeira classe
"""

def greeting(msg, name):
    return f'{msg}, {name}!'

def execute(function, *args):
    return function(*args)

print(execute(greeting, 'Good Morning', 'Gian'))
print(execute(greeting, 'Good Morning', 'Maria'))