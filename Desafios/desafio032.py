
from datetime import date

print('===== Desafio 032 =====')

ano = int(input('Digite o ano desejado, 0 para ano atual: '))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} NÃO é Bissexto')