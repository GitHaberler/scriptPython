print('===== Desafio 031 =====')

dist = float(input('Digite a distancia percorida rm KM: '))

if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.50

print(f'O valor da sua a viagem é de \033[1;30;40mR$ {valor:.2f}\033[m')
