# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.73
euro = real / 4.22
print('Com R$ {:.2f} você pode converter para US$ {:.2f} ou € {:.2f}.'.format(real, dolar, euro))
