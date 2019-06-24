km = float(input('Quantos Kilômetros você percorreu? '))

if km <= 200:
    preco = '0,50'

    res = km * 0.50

else:
    preco = '0,45'
    res = km * 0.45

print('Como você andou {:.0f} km, deve pagar R$ {:.2f}, sendo {} cada km.'.format(km, res, preco))
