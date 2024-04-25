import os
os.system('cls || clear')

#Elabore um algoritmo para ler o nome de um aluno, sua idade e as três notas. Calcular a média do aluno.
nome = str(input('Digite seu nome: '))
nota01 = int(input('Digite sua nota01: '))
nota02 = int(input('Digite sua nota02: '))
nota03 = int(input('Digite sua nota03: '))

media = (nota01 + nota02 + nota03) / 3

print('\n<---Exibir resultados--->')
print(f'Nota01: {nota01}')
print(f'Nota02: {nota02}')
print(f'Nota03: {nota03}')
print(f'Media: {media}')

if media >= 7:
    print('Você está aprovado!')
else:
    print('Você esttá reprovado!') 