# Variáveis e tipos de dados 'básicos'

# Uma variável é um espaço na memória onde armazenamos um valor.


# Variável do tipo string (texto), sempre entre aspas ("" ou '')
nome = 'Matheus'
idade = 27       # Var do tio inteiro(núm sem casas decimais)
altura = 1.80    # Var do tipo float(núm com casas decimais)
dev = True       # Var do tipo booleano, valores lógicos (true/false)

# print(f'Olá, {nome}! Você tem {idade} anos e mede {altura}m.')


nome = input('Digite seu nome: ')  # Entrada de textp
# Entrada de texto convertida para int
idade = int(input('Digite dua idade: '))
altura = float(input('DIgite sua altura: '))  # Entrada convertida para float
cidade= input('Digite sua cidade')


print(f'Olá, {nome}! Você tem {idade} anos, mora em {cidade} e mede {altura}m. ')
