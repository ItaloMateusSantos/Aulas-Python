import os

os.system ('cls || clear')

QUANTIDADE_NOTAS = 3
soma = 0
nota = 0
media = 0 

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota (entre 0 e 10): '))

        if nota < 0 or nota > 10:
            print('Nota inválida. Por favor, tente novamente \n')
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    print('Você está aprovado!')
elif media >= 5:
    print('Você está em recuperação!')
else:
    print('Você está reprovado!')
print(f'Média: {media}')


