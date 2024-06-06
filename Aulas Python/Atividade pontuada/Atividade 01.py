#Declarando bibliotecas
import os
import time
import sys
os.system ('cls || clear')

# Inicializando  as variáveis
numeros = []
numero = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
maior_numero = 0
menor_numero = sys.maxsize
soma_pares = 0
soma_impares = 0
media_pares = 0
media_impares = 0
media_geral = 0 
i = 0

#Lendo os números
for i in range(5):
    
    numero =int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
    
# Processando se é número par ou impares.
    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1
        soma_impares += numero

#Processando se um número é positivo ou negativo:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
        
# Calculando o maior e menor número
    maior_numero = max(numero, maior_numero)
    menor_numero = min(numero, menor_numero)
    
# Calculando a média geral dos números.
    media_geral += numero / 5 
    
    if pares == 0:
        media_pares = 0
    else:
        media_pares = soma_pares/pares
    
    if impares == 0:
        media_impares = 0
    else:
        media_impares = soma_impares/impares

# Imprimindo as estatísticas
print("\n===Apresentação dos dados===")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
print(f"A media de pares são: {media_pares}")
print(f"A média de impares são: {media_impares}")
print(f"A média geral é: {media_geral}")

#Ordem inversa
print('\n===Ordem inversa===')
numeros.reverse()
print(numeros)