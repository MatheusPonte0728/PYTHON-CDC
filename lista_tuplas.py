# Listas e Tuplas

# Tipos de dados que armazanam múltiplos valores, mas têm
# diferenças importantes:

# LIstas:
#  - Modificável (pode adicionar, remover e alterar valorse)
# - Mais lenta
# - Quando precisamos modificar dados

# Tuplas:
# - Não moificável (uma vez criada, não pode ser alterada)
# - Mais rapida
# - Quando os dados não devem ser alterados

# Lista
# Definida entre colchetes [] e pode armazenar diferentes tipos de dados

# frutas = ["maçã", "banana", "laranja"]
# numeros = [1, 2, 3, 4, 5]
# misturada = ["Python", 3.14, True]

# Acessando elemtos da lista

# print(frutas[0])  # "maçã"
# print(frutas[1])  # "banana"
# print(frutas[-1])  # "laranja" (indice negativo conta de tras para frente)

# Alterando um valor na lista
# print(frutas)

# frutas[1] = "uva"
# print(frutas)  # ["maçã", "uva", "laranja"]

# ADicionando elementos a lista

# append(): adiciona um item ao final
# insert(): adiciona um item em uma posição especíica


# numeros = [1, 2, 3]
# print(numeros)

# numeros.append(4)

# print(numeros)  # [1, 2, 3, 4]

# .insert(1, 10)  # (posição, valor)
# (numeros)  # [1, 10, 2, 3, 4] (inseriu o 10 na posição 1)

# Removendo elementos da lista

# reomce(): remove um item pelo valro
# pop(): remove um item pelo indice (ou o ultimo item
# se nenhum indeice for passado)

# frutas = ["maçã", "banana", "laranja", "uva"]
# nfrutas.remove("banana")
# print(frutas)

# frutas.pop(0)
# print(frutas)

# frutas.pop()
# print(frutas)

# Tuplas
# Tuplas são como listas, mas são imutáveis.
# Elas são criadas com parenteses ().

# cores = ("vermelho", "azul", "verde")
# numeros = (1, 2, 3, 4, 5)

# Acessando elementos
# (cores[0])  # "vermelho"
# print(cores[-1])  # "verde"

# Tentando modifica uma tuplas (Erro!)
# cores[1] = "amarelo" # X Isso gera um erro,
# pois tuplas são imutaveis!

# Convertendo entre lista e tupla
# Podemos converter uma tupla para uma lista e modificar os elemntos

tupla = (1, 2, 3)
lista = list(tupla)   # Converte para lista
lista.append(4)     # Modifica a lista
tupla = tuple(lista)  # Converte de volta para tupla
print(tupla)  # (1, 2, 3, 4)

# Quando usar tuplas?
#  - Quando queremos garantis que valores não sejam alterados.
#  - Para armazenar dados fixos como coordenadas, meses do ano,
#    dias da semana etc.

meses = ("janeiro", "Fevereiro", "Março", "Abril")
print(meses[2])  # "Março"
