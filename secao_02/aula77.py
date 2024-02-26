# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiply_numbers(quantity):
    def multiply(number):
        return f'{number} x {quantity} = {number * quantity}'
    return multiply

two_times = multiply_numbers(2)
three_times = multiply_numbers(3)
four_times = multiply_numbers(4)

print(two_times(2))
print(three_times(6))
print(four_times(12))