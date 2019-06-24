print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)

r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os seguimentos acima PODEM FORMAR um triângulo!')

else:
    print('Os seguimentos acima %s PODEM FORMAR um triângulo!' % r1)


