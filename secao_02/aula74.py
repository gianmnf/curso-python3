# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def numero_par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'

print(numero_par_impar(2), numero_par_impar(3))