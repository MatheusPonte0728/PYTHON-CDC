# jogo da adivinhação
# no jogo o usuario precisa adivinhar um numero sevreto
# ele pode tentar várias vezes até acertar.

numero_secreto = 10
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar um número de 1 a 10: "))  # Nessa
    # linha de código o usuario digita um numero e ele é convertido em interio
    # ja que a função input sem vai ler string

    if tentativa < numero_secreto:  # aqui tem um if para verificar se a
        # tentativa é menor que o numero secreto
        print("O número secreto é maior!")
    elif tentativa > numero_secreto:  # aqui tem um elif para verificar se a
        # tentativa é maior que o numero secreto
        print("O número secreto é menor!")
    else:  # aqui tem um else para verificar se a tentativa é igual ao numero
        # secreto
        print("Parabéns! Você acertou o número secreto!")
