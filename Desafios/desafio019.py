import random
print('===== Desafio 019 =====')

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print(f'O escolhido foi: {escolhido}')
