print('===== Desafio 036 =====')

casa = float(input('Valor da Casa R$ '))
salario = float(input('Salario do comprador R$ '))
anos = int(input('Quantos anos de financiamento? '))

tetoPrestacao = salario * 30 /100

prestacao = casa / anos * 12

if prestacao > tetoPrestacao:
    print('Lamento emprestimo negado!!!')
else:
    print('Parabens o emprestimo foi aprovado!')
