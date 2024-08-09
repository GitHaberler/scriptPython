print('===== Desafio 042 =====')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triângulo')
elif (a == b) and (a == c):
    print('Equilátero')
elif (a == b) or (a == c) or (b == c):
    print('Isósceles')
else:
    print('Escaleno')