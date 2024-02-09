"""
Aprimoramentos exercício CPF
"""
import re
import sys

entrada = input('CPF: ')
cpf_enviado = re.sub(r'[^0-9]','', entrada)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

parte_1 = cpf_enviado[:9]

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

if cpf_enviado == cpf_gerado:
    print(f'CPF {cpf_enviado} é válido')
else:
    print('CPF Inválido')