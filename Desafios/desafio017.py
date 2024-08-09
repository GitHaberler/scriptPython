from math import sqrt, hypot
print('===== Desafio 017 =====')

cat_adj = float(input('Informe o Cateto Adjacente: '))
cat_ops = float(input('Informe o Cateto Opsto: '))

#hipotenusa = sqrt(cat_adj ** 2 + cat_ops ** 2)
hipotenusa  = hypot(cat_adj, cat_ops)
print(f'A hipotenusa deste triangulo é: {hipotenusa}')
