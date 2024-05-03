import os
os.system('cls || clear')

print('=== Solicitando dados ao ususário===\n')
numero = int(input('Digite até 5 números: '))

for i in range(1,6):
    if numero % 2 == 0:
       print('Esse númeo é impar')

    else:
        print('Esse número é par')


