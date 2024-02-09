import random
import sys

entrada = input('Digite quantos CPFs deseja gerar: ')

if entrada.isdigit:
    for _ in range(int(entrada)):
        parte_1 = ''

        for i in range(9):
            parte_1 += str(random.randint(0, 9))

        contador_1 = 10
        valor_digito_1 = 0

        for digito in parte_1:
            valor_digito_1 += int(digito) * contador_1
            contador_1 -= 1
        digito_1 = (valor_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        parte_2 = parte_1 + str(digito_1)

        contador_2 = 11
        valor_digito_2 = 0

        for digito in parte_2:
            valor_digito_2 += int(digito) * contador_2
            contador_2 -= 1

        digito_2 = (valor_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado = f'{parte_1}{digito_1}{digito_2}'

        print(cpf_gerado)
else:
    print('Valor inválido')
    sys.exit()
