print('-=-' * 15)
print('Analisador de Triângulos 2.0')
print('-=-' * 15)

r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))


if r1 == r2 == r3:
    print('O seguimento acima formará um triângulo equilátero!')
elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r2 != r1 or r1 == r3 != r2:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
        print('O seguimento acima formará um triângulo isósceles!')
        exit()
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')
elif r1 != r2 != r3:
    print('O seguimento acima formará um triângulo escaleno!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    a = 'Os seguimentos acima PODEM FORMAR um triângulo!'
    print(a)
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')

