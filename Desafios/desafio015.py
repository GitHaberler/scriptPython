print('===== Desafio 015 =====')

km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias?'))
total = (60 * dias) + (0.15 * km)

print(f'O valor total do aluguel é de: R$ {total:2}')
