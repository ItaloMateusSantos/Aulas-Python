import os

os.system ("cls || clear")

nota = 0
media = 0

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print('\n=== Exibir Resultados====')
print(f'Primeira Nota {nota1}')
print(f'Segunda Nota {nota2}')
print(f'Terceira Nota {nota3}')
print(f'Sua média é: {media}')

if media >= 7:
    print('Você foi aprovado!')

elif media >=4:
    print('Você está em recuperação!')

else:
    print('Você foi reprovado!')



