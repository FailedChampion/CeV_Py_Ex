tex = input('Escreva algo: ').strip()
up = tex.upper()
print('Observando sua frase...')
print('\nA letra a aparece {} vezes, '.format(up.count('A')))
print('Ela aparece pela primeira vez no caractere {}'.format(up.find('A') + 1))
print('E aparece pela última vez no caractere {}.'.format(up.rfind('A') + 1))
print(len(up))
