import os
os.system('cls || clear')

maca = int(input('Informe quantas maças deseja [kg]: '))
morango = int(input('Informe quantos morangos deseja [kg]: '))


if maca < 5:
    maca = 2.50
else:   
    match = 2.20

if morango < 5:
    morango = 1.80
else:
    morango = 1.50

pesoTotal = maca + morango
subTotal = (macas + morango) + (maca * morango)

if pesoTotal > 8 or subTotal . 25:
    desconto = subtotal * 0.10

totalPagar = subtotal - desconto

print('Total a pagar: (morango)')