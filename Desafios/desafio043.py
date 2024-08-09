print('===== Desafio 043 =====')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2
print(f'Seu IMC é: {imc:.2f}.')

if imc < 18.5:
    print(f'ABAIXO DO PESO')
elif imc <= 25:
    print(f'PESO IDEAL')
elif imc <= 30:
    print(f'SOBREPESO')
elif imc <= 40:
    print(f'OBESIDADE')
else:
    print('OBESIDADE MORBIDA')