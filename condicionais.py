# CONDICIONAIS

# são estruturas que permitem ao nosso programa tomar decisões com base
# em determinadas condições. Em outras palavras, o program pode executar
# ações diferentes dependendo de uma situação específica.

# Exemplo:

# Você está em uma cafeteria e está com pouca grana.
# O capuccino custa 10 reais, café com leite 7 e o café simples 4.

# Se você tiver 10 reias ou mais na carteira, pode pedir o capuccino.
# Se Você tiver 7 reais ou mias, pode pdir o café com leite.
# se não, pede o café simpes



# Sintaxe básica no Python!

# if - 'Se'
# else - 'Se não'
# elif - se + se não

# if condição: 
    # Código a ser executado se a condição for verdadeira
# elif outra_condição:
    # Código executado se aprimeira condição for falsa, mas essa verdadeira
# else:
    # Código executado se nenhuma das condições anteriores for verdadeira



# EXEMPLOS

#Verificando a idade para entrada em um evento (18 ANOS)

idade = int(input('Digite sua idade ')) #Usuário digita sua idade

if idade >=18:
    print('Você pode entrar no evento')
else:
    print('Desculpe, você ainda não tem idade suficiente para entrar.')