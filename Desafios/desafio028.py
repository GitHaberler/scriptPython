import random

print('===== Desafio 028 =====')

num = random.randint(0, 5)
print('=#=' * 20)
chute = int(input('Adivinhe o numero entre 0 e 5: '))
print('=#=' * 20)5
if chute == num:
    print('Parabens! Você acertou!')
else:
    print(f'Lamento voce errou! Pensei no numero {num} você disse {chute}.')
