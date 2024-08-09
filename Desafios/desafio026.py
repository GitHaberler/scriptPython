print('===== Desafio 026 =====')

frase = str(input('Digite uma frase: ')).strip().upper()

print(f"A letra A aparece: {frase.count('A')} vezes na frase")
print(f'Ela aparece a primeira vez na posição: {frase.find('A')}')
print(f'Ela aparece a ultima vez na posição: {frase.rfind('A')}')