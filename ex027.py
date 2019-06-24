nome = str(input('Insira seu nome completo: ')).strip()
sp = nome.split()


print('O seu primeiro nome é: {},'.format(sp[0]))
print('E seu último nome é {}.'.format(sp[len(sp)-1]))
