# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Insira uma distância em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a \n{:.3f} Km \n{:.2f} Hm \n{:.1f} Dam'.format(m, (m / 1000), (m / 100), (m / 10)))
print('{:.0f} Dm \n{:.0f} Cm \n{:.0f} mm'.format(dm, cm, mm))

