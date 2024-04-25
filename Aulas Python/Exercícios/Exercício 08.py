import os
os.system ('cls || clear')

#Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar.
#Considere a regra que menor de 18 anos e maior que 65 anos não são obrigrados a votar.

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade <= 18:
    print('Não será obrigado a vorta!')
elif idade >= 65:
    print('Não é orbigrado  a votar!')
else:
    print('O voto é obrigatório para você.')

print('===FIM===')
