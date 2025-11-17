# Variáveis e tipos de dados 'básicos'

# Uma variável é um espaço na memória onde armazenamos um valor.


nome = 'Matheus' # Variável do tipo string (texto), sempre entre aspas ("" ou '')
idade = 27       # Var do tio inteiro(núm sem casas decimais)
altura = 1.80    # Var do tipo float(núm com casas decimais)
dev = True       # Var do tipo booleano, valores lógicos (true/false)

# print(f'Olá, {nome}! Você tem {idade} anos e mede {altura}m.')


nome = input('Digite seu nome: ') # Entrada de textp
idade = int(input('Digite dua idade: ')) # Entrada de texto convertida para int
altura = float(input('DIgite sua altura: ')) # Entrada convertida para float

print(f'Olá, {nome}! Você tem {idade} anos e mede {altura}m. ')
