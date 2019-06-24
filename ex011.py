# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m².'.format(lar, alt, (lar * alt)))
print('Para pintar essa parede, você precisará de {:.1f}L de tinta.'.format(lar * alt / 2))