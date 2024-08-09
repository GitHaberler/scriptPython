import math

print('===== Desafio 018 =====')

angulo = float(input('Informe o angulo desejado: '))
angulo = math.radians(angulo)
cos = math.cos(angulo)
sen = math.sin(angulo)
tan = math.tan(angulo)

print(f'O SENO é: {sen}')
print(f'O COSSENO é: {cos}')
print(f'A TANGENTE é: {tan}')
