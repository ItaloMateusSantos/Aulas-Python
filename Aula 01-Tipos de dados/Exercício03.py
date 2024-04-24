import os
os.system('cls || clear')

#Elabore um arquive para ler o nome de uma aluno, sua idade e suas notas.
nome = str(input('Digite seu nome: '))
nota01 = int(input('Digite sua nota01: '))
nota02 = int(input('Digite sua nota02: '))

media = (nota01 + nota02) / 2

print('\n<---Exibir resultados--->')
print(f'Nota01: {nota01}')
print(f'Nota02: {nota02}')
print(f'Media: {media}')
