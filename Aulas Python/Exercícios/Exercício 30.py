import os
os.system ('cls || clear')

#Iniciando variável 
resultado = False

while True:
    os.system ('cls || clear')
    #Solicitando dados ao susário.
    a = int(input('Digite o primeiro número: '))
    operador = input('Digite o operador: + - * /: ')
    b = int(input('Digite o segundo número: '))

    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*':
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
            input('Operador inválido')

print(f'\nResultado: {resultado}')