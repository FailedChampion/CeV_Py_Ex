# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('E quantos kilômetros percorreu? '))
calcdia = dia * 60
calckm = km * 0.15

print('\nComo você percorreu {} Km e ficou {} dia(s) com o carro...'.format(km, dia))
print('\nDeve pagar R$ {:.0f} pelos dias e R$ {:.2f} pelos Km percorridos,'.format(calcdia, calckm))
print('\ndando no total R$ {:.2f}.'.format(calcdia + calckm))
