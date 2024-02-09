"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

""" def Print(a, b, c):
    print('Várias 1')
    print('Várias 2')
    print('Várias 3')
    print('Várias 4') """

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem Nome'):
    print(f'Olá, {nome}!')

saudacao('Gian')
saudacao('Maria')
saudacao()
