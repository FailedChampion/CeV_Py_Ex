from datetime import date

data = date.today()
ano_nas = int(input('Qual seu ano de nascimento? '))

if data.year - ano_nas - 18 == 1:
    print('Seu tempo de alistamento já se passou por 1 ano. Vá atrás enquanto dá!')

elif data.year - ano_nas > 18:
    print('Seu tempo de alistamento já passou por {} anos. Vá atrás!'.format((data.year - ano_nas) - 18))

elif data.year - ano_nas == 18 or data.year - ano_nas == 17:
    print('Está na hora de você se alistar! vá para a prefeitura mais próxima para mais '
          'informações.')

elif data.year - ano_nas == 16:
    print('Você é muito novo ainda! falta 1 ano para você se alistar. Prepare-se!')

elif data.year - ano_nas == 15:
    print('Você é muito novo ainda! falta 2 anos para você se alistar. Prepare-se!')

elif data.year - ano_nas == 14:
    print('Você é muito novo ainda! falta 3 anos para você se alistar. Prepare-se!')

elif data.year - ano_nas == 13:
    print('Você é muito novo ainda! falta 4 anos para você se alistar. Prepare-se? Tem tanto tempo ainda...')

elif data.year - ano_nas < 13:
    print('Acho que você está muito novo para pensar em se alistar, não?')
