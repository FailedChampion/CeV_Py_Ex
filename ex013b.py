prod = float(input('Qual o preço do produto? R$ '))
avis = prod - (prod * 0.1)
parc = prod + (prod * 0.08)
print('Se pagar a vista, recebe desconto de 10% de desconto, dando R$ {:.2f} no total.'.format(avis))
print('\n se pagar parcelado, o preço do produto aumenta em 8%, dando R$ {:.2f} no total.'.format(parc))
