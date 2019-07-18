#  Desenvolva um programa que leia o primeiro termo
#  e a razão de uma PA. No final, mostre os 10
#  primeiros termos dessa progressão.
from emoji import emojize

pt = str(input('Primeiro termo: '))
rz = str(input('Razão: '))
rz = int(rz)
pt = int(pt)
ndf = rz

print('{}'.format(pt), end=' ')
for d in range(9):
    print(emojize(':arrow_right: {}'.format(rz + pt), use_aliases=True), end=' ')
    for c in range(1):
        rz += ndf
print(emojize(':arrow_right: ACABASTES', use_aliases=True), end=' ')