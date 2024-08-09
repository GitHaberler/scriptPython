print('===== Desafio 022 =====')

nome = str(input('Digite seu nome completo: ')).strip()

tamanho = (len(nome) - nome.count(' '))
listaNomes = nome.split()
primeiro = listaNomes[0]

print(f'Analisando seu nome ....')
print(f'Seu nome em maiusculas é: {nome.upper()}')
print(f'Seu nome em minusculas é: {nome.lower()}')
print(f'Seu nome tem ao todo: {tamanho} letras')
print(f'Seu primeiro nome é: {primeiro} e ele tem {len(primeiro)} letras')
