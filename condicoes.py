n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é : {media}')

if media >= 6:
    print('Parabens, voce passou!')
else:
    print('Lamento voce reprovou, estude mais!')
    