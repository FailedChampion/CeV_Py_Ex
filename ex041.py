from datetime import  date

data = date.today()

ano_nas = int(input('Qual seu ano de nascimento? '))

if data.year - ano_nas <= 9:
    print('MIRIM')

elif data.year - ano_nas <= 14:
    print('INFANTIL')

elif data.year - ano_nas <= 19:
    print('JUNIOR')

elif data.year - ano_nas <= 20:
    print('SÊNIOR')

elif data.year - ano_nas <= 70:
    print('MASTER')

elif data.year - ano_nas <= 90:
    print('APOSENTADO')

else:
    print('MORTO :)')


print(data.year - ano_nas)

