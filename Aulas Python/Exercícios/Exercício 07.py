import os
os. system('cls || clear')

#Elabore um algoritmo para receber login e senha de um usuário.
#Caso o usuário e senha estejam corretos, mostre a mensagem "Bem vindo!", caso contrário, mostre a mensagem de "Login e senha inválidos"

usuario = str(input('Digite o seu nome de usuário: '))
senha = int(input('Digit a sua senha: '))

if usuario == 'Mateus' and senha == 87:
    print('Seja bem vindo!')
else: 
    print('Login ou senha inválidos.')

