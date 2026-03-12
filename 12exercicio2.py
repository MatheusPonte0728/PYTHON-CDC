# Simulando um caixa eletrônico

# O usuário tem um saldo inicial de R$500,00 e pode sacar o dinheiro até zerar
# O saldo ou encerrar o programa

saldo = 500

while saldo > 0:  # Aqui indica que o programa vai ficar rodando enquanto a
    #  condição for verdadeira, saldo > que 0.
    saque = float(input("Informar o valor do saque (ou digite 0 para sair): "))
    # Aqui o usuário digita o valor do saque e ele é convertido em float para
    # permitir valores decimais.
    if saque == 0:
        break  # Aqui tem um break para encerrar o programa se o usuário
    #  digitar 0, condição inposta no if acima (saque == 0).
    if saque > saldo:
        print("Saldo insuficiente! Saque não efetuado")  # Aqui a condição
        # verifica se o valor do saque é maior que o saldo, se não o programa
        # exibe uma mensagem de saldo insuficiente e o saque não é efetuado.
    else:
        saldo -= saque
    print(f"Saque efetuado! Novo saldo R${saldo:.2f}")  # Aqui o programa
    # exibe uma mensagem de saque efetuado e novo saldo formatado com duas
    # casas decimais.
print("Operação finalizada!")
