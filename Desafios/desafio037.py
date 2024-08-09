print('===== Desafio 037 =====')

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] BINARIO
      [ 2 ] OCTAL
      [ 3 ] HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida!')
