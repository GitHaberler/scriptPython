print('===== Desafio 004 =====')
msg = input('Digite algo:')

print(f'=====================')
print(f'Voce digitou: {msg}')
print(f'A mensagem é da classe? {type(msg)}')
print(f'A mensagem foi digitada? {msg}')
print(f'A mensagem é numerica? {msg.isnumeric()}')
print(f'A mensagem é alfabética? {msg.isalpha()}')
print(f'A mensagem é alfanumerica? {msg.isalnum()}')

