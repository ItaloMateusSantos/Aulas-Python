import os
os.system('cls || clear')

print('=== Solicitando dados ao ususário===\n')
numero = int(input('Ditite um número entre 1 e 120: '))

for i in range(1,120):
    if numero % 2 != 0:
       print('Esse númeo é impar')

    else:
        print('Esse número é par')

    break
