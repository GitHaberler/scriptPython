from datetime import date

print('===== Desafio 041 =====')

nasc = int(input('Digite o ano de seu nascimento: '))

idade = date.today().year - nasc

if idade <= 9:
    print(f'Voce tem {idade} anos, esta no Mirim')
elif idade <= 14:
    print(f'Voce tem {idade} anos, esta no Infantil')
elif idade <= 19:
    print(f'Voce tem {idade} anos, esta no Junior')
elif idade <= 25:
    print(f'Voce tem {idade} anos, esta no Senior')
else:
    print(f'Voce tem {idade} anos, esta no Master')
