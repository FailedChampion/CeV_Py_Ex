km = float(input('Qual é a distância da viagem? '))

if km <= 200:
    preco = '0,50'

    res = km * 0.50

else:
    preco = '0,45'
    res = km * 0.45

print('Você está prestes a começar uma viagem de {:.0f} Km.'.format(km))
print('E o preço da sua passagem será de R$ {:.2f}.'.format(res))