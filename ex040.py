n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))

med = (n1 + n2) / 2
print(med)

if med <= 5:
    print('REPROVADO')

elif med > 5.1 and med <= 6.9:
    print('RECUPERAÇÃO')

else:
    print('APROVADO')