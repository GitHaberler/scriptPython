print('===== Desafio 024 =====')

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()

tem = cidade[:5] == 'SANTO'

print(f'Tem a palavra Santo em {cidade}: {tem}')
