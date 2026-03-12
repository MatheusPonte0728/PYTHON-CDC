# Laçõs de Reptição (for e while)

# Imagine que você precisa pedir para alguem contar de 1 a 100
# e escrever cada npumero em um papel.
# Fazer isso manuelamente seria muito cansativo e demorado, né?

# Agora, imagine que um programa pode fazer essa contagem automaticamente,
# sem precisar repetir o mesmo comando 100 bezes.
# É exatemnte isso que os laços de reptição fazem!

# Os laços de reptição são usados para executar um bloco de código várias
# vezes, até que uma condição seja atingida.

# Python tem dois tipos princiais de laços:

# for - Quando sabemos quantas vezes queremos repetir algo.
# while - Quando queremos repetir algo até que uma condição se torne falsa.

# FOR

# o FOR é usado quando sabemos quantas vezes queremos repetir um bloco
# de código. Ele percorre uma sequência de valores, como uma lista, um
# intervalo de números ou até mesmo letras de uma palavra.

# Estrutura

# for variavel in sequencia:
# Código a ser repetido

# contando de 1 a 5 com FOR

# [1, 2, 3, 4, 5]
# for numero in range(1, 101):
#    print(numero)

# O range(1, 6) gera os número de 1 a 5, o ultimo número do range não aparece


# Percorrendo uma lista de compras

# compras = ["Arroz", "Feijão", "Leite", "Ovos"]

# for item in compras:
#    print(f"Comprar {item}")

# Percorrendo as ltras de uma palavra

# palavra = "COMUNIDADE"

# for letra in palavra:
#   print(letra)

# WHILE

# O while é usado quando não sabemo quantas vezes a repetição vai acontecer,
# mas sabemos a condição que deve ser atendida para continuar.

# while condição:
# código a ser reptido enquanto a condição for verdadedira


# obs: CUidado com loops infinitos!
# Se a condição nunca mudar para False, o código nunca para de rodas.

# COntagem regressiva

# contador = 10

# while contador > 0:
#    print(f"{contador} segundos")
#   contador -= 1  # Diminui 1 d contador a cada rpetição

# print("Fogo!")

# Pedindo senha até acertar

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso permitido!")
