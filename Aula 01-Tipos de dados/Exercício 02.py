import os
os.system('cls || clear')

#Cálcule um algorimo para ler dois números e em seguida apresentar a soma dos dois
numero01 = int(input('Digite o número01: '))
numero02 = int(input('Digite o número02: '))

soma = numero01 + numero02
subtracao = numero01 - numero02
multiplicacao = numero01 * numero02
divisao = numero01 / numero02

print('\n<---Exibir resultados--->')
print(f'numero01: {numero01}')
print(f'numero02: {numero02}')
print(f'\nSoma: {soma}')
print(f'Subtracao: {subtracao}')
print(f'Multiplicacao: {multiplicacao}')
print(f'Divisao: {divisao}')

