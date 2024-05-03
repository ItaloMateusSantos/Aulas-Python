import os
os.system('cls || clear')

print('=== Solicitando dados do usuário ====\n')
numero = int(input('Digite um número entre 100 até 120: '))

for i in range(100, 121):
    if numero % 2 == 0:
        print('Esse número é par') 
    else:
        print('Esse número é impar')

    break