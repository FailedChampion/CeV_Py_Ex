from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
h = hypot(n1, n2)
print('A hipoternusa vai medir {:.2f}'.format(h))
