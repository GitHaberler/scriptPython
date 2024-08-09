print('===== Desafio 040 =====')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print(f'Parabens aprovado com média {media}!')
elif media < 7.0 and media >= 5.0:
    print(f'Voce esta em recuperação com média {media}, estude mais para passar')
else:
    print(f'Lamento mas voce esta Reprovado, sua media ficou em {media}!')

