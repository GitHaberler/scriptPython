# Opcoes de texto

frase = 'Curso em Video Python'

print(f'Texto na posicao 0: {frase[0]}')
print(f'Texto da Posicao 0 ate a Quarta: {frase[0:5]}')

print(f'Encontre Video: {frase.find('Video')}')
print(f'Encontre Video: {frase.find('android')}')

if 'Curso' in frase:
    print('TRUE')

print(frase.replace('Python','Android'))

print(frase.upper())

print(frase.capitalize())

print(frase.title())

frase.split()
'-' join(frase)