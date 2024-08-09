from datetime import date
print('===== Desafio 039 =====')

ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Voce deve se alistar este ano')
elif idade > 18:
    print('Voce já devia estar alistado!')
else:
    print(f'Voce ainda tem {18 - idade} para ter de se alistar')
    