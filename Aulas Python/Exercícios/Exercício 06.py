import os
os.system('cls || clear')

#Elabore um algoritmo para receber dois inteiros como entrada do teclado e escreva na tela:
#A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado.

numero01 = int(input('Digite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))

soma = numero01 + numero02
multiplicacao = numero01 * numero02
media = (numero01 + numero02) / 2

maiorNumero = max(numero01, numero02)
menorNumero = max(numero01, numero02)

if numero01 > numero02:
    maiorNumero = menorNumero
else:
    maiorNumero = numero02

if numero01 < numero02:
    menorNumero = numero01
else:
    menorNumero = numero01


print('\n<---Exibindo Resultados--->')
print(f'Numero01: {numero01}')
print(f'Numero02: {numero02}')
print(f'Soma: {soma}')
print(f'Multiplicaçâo: {multiplicacao}')
print(f'Média: {media}')
print(f'Maior número {maiorNumero}')
print(f'Menor número: {menorNumero}')