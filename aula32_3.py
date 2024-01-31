"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu nome: ')
entrada_length = len(entrada)

if entrada_length <= 4:
    print('Seu nome é curto')
elif entrada_length >= 5 and entrada_length <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')