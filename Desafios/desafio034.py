print('===== Desafio 034 =====')

salario = float(input('Qual o salario? R$'))

if salario > 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f'Seu novo salario será de: R$ {novo:.2f}')
