print('===== Desafio 033 =====')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

lista = [n1, n2, n3]
ordenada = sorted(lista)
print(ordenada)

print(f'O menor valor é o: {ordenada[0]}')
print(f'O maior valor é o: {ordenada[len(ordenada)-1]}')

