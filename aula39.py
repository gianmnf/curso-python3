"""
Iterando strings com while
"""
nome = 'Gian Michel'
total_nome = 0

nova_string = ''

while total_nome < len(nome):
    nova_string += f'*{nome[total_nome]}'
    total_nome += 1

nova_string += '*'
print(nova_string)