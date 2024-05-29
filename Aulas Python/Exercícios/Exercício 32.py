import os
os.system('cls || clear')

resultado = False

#Menu
print('===MENU===')
print('Opção 1 >> Picanha')
print('Opção 2 >> Lasanha')
print('Opção 3 >> Estrogonoff')
print('Opção 4 >> Bife acebolado')
print('Opção 5 >> Pão com ovo')


while True:
    os.system('cls || clear')
    menu = int(input('Digite uma opção no menu de 1 a 5'))

    match(menu):
        case 1:
            resultado = 'Produto >> Picanha | Valor >> R$ 25,00' 
            break
        case 2:
            resultado = 'Produto >> Lasanha | Valor >> R$ 20,00'
            break
        case 3:
            resultado = 'Produto >> Estrogonoff | Valor >> R$ 18,00'
            break
        case 4:
            resultado = 'Produto >> Bife Acebolado | Valor >> R$ 15,00'
            break
        case 5:
            resultado = 'Produto >> Pão com ovo | Valor >> R$ 5,00'
            break
        case _:
            input('Opção selecionada inválida, por favor selecione um opção.')

if resultado:      
    print(f'O prato selecionado foi: {resultado}')   


    