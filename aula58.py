import os
"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    entrada = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ')

    if len(entrada) > 1:
        print('Digite uma opção válida')

    if entrada == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif entrada == 'a':
        indice_str = input('Digite o índice: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um valor int')
        except IndexError:
            print('Indice não existe na lista')
    elif entrada == 'l':
        os.system('cls')
        if len(lista) > 0:
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('Lista vazia.')
    elif entrada == 's':
        break