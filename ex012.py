# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual o preço do produto? R$ '))
calc1 = preco -(preco * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% agora vai custar R${:.2f} '.format(preco, calc1))
