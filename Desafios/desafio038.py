print('===== Desafio 038 =====')

num1 = int(input('Digite um inteiro: '))
num2 = int(input('Digite outro inteiro: '))

if num1 == num2:
    print('Os numeros digitados são iguais!!!')
elif num1 > num2:
    print(f'O {num1} é maior do que o {num2}.')
else:
    print(f'O {num2} é maior do que o {num1}.')
