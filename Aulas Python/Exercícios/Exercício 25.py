import os
os.system ('cls || clear')

QUANTIDADE_NOTAS = 3

notas = []
soma = 0 
media = 0

for i in range (QUANTIDADE_NOTAS):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

for i in range(QUANTIDADE_NOTAS):
    print(f'Nota: {notas[i]}')
 
media = sum(notas) / QUANTIDADE_NOTAS

print('\n===Exibir os resultados===')

print(f'Media das notas {media}')