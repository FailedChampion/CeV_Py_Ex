from playsound import playsound
nome = str(input('Qual o seu nome?')).strip()
if 'SILVA' in nome.upper():
    print('Olha só, você possui "Silva" no seu nome!')
    playsound('m.mp3')

else:
    print('Você não possui "Silva" no seu nome...')
    playsound('ff.mp3')

print(nome)
