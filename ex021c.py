import emoji
from playsound import playsound

cal =  str(input('Quanto é 5 + 5?   '))
if cal == '10':
    print(emoji.emojize(':smiley: Parabéns, você acertou! :smiley:', use_aliases=True))
    playsound('m.mp3')
else:
    print(emoji.emojize(':skull: You are gonna have a bad time. :skull:', use_aliases=True))
    playsound('me.mp3')
