import os
os.system('cls || clear')

valor_produto = int(input('Digite o valor do produto: R$ '))

#Solicitando dados do usuário
print('Escolha a forma de pagamento: ')
print(' 1 - Pagamentos à vista')
print('2 - Pagamento à prazo')
forma_pagamento = int(input('Digite a opção (1 ou 2):'))

#Pagamento à vista
if forma_pagamento == 1:
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print('\nForma de pagamento: À vista')
    print(f'Valor do produto: R$ {valor_produto: .2f}')
    print(f'Valor do desconto: R$ {desconto: .2f}')

elif forma_pagamento == 2:
    parcelas = int(input('Digitee a quantidade de parcelas:'))
    valor_parcela = valor_produto / parcelas
    print('\nForma de pagamento a prazo')
    print(f'Valor do produto: R$ {valor_produto: .2f}')
    print(f'Quantidade de parcelas: {parcelas}')
    print(f'Valor da parcela: R$ {valor_parcela:.2f}')
    print(f'Total parcelado: R$ {valor_produto: .2f}')

else:
    print('Opção inválida. Por favor, escolha opção 1 ou 2.')    
