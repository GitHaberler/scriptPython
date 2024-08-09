print('===== Desafio 029 =====')

velocidade = float(input('Informe a velocidade: '))

if velocidade < 80:
    print('Parabens! Voce esta dentro do limite!')
else:
    excesso = velocidade - 80
    multa =  excesso * 7
    print(f'Voce exedeu o limite! Sua multa é de R$ {multa:.2f}.')
    print('Dirija com mais cuidado.')
