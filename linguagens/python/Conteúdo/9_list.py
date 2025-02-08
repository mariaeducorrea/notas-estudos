# Criando lista
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]

# Acessando elementos por index
print(numeros[0])
print(numeros[3])

# Fatiamento 
print(numeros[0:2])
print(numeros[2:4])

# Adicionar elementos na lista
numeros.append(10)

# Adicionar posição e valor a ser adicionado
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]
numeros.insert(1,5) 
print(numeros)

# Remover elemetos
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]
numeros.remove(5)
print(numeros)

# Remove item por indice
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]
numeros.pop(1) 
print(numeros)

# Alterar elemento por indice
numeros[1] = 15  # altera valor e uma posiçãoe especifica

# Limpar toda a lista
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]
numeros.clear()
print(numeros)

# Verificar se um elemento está na lista
numeros = [1, 2 , 3, 4, 5, 6, 10, 20]
print(20 in numeros)  # True
print(60 in numeros)  # False

# Ordenar uma lista em ordem crescente
lista = [50, 10, 40, 30, 20]
lista.sort()
print(lista)  # [10, 20, 30, 40, 50]

# Ordenar em ordem decrescente
lista = [50, 10, 40, 30, 20]
lista.sort(reverse=True)
print(lista)  # [50, 40, 30, 20, 10]

# Reverter a lista
lista = [50, 10, 40, 30, 20]
lista.reverse()
print(lista)  # [10, 20, 30, 40, 50]


# Iterar com for
lista = [50, 10, 40, 30, 20]
for item in lista:
    print(item)

# Usar enumerate para obter índices e valores
lista = [50, 10, 40, 30, 20]
for i, valor in enumerate(lista):
    print(f"Índice {i}: Valor {valor}")

# Soma, máximo, mínimo e tamanho
lista = [10, 20, 30, 40, 50]
print(sum(lista))  # 150
print(max(lista))  # 50
print(min(lista))  # 10
print(len(lista))  # 5

# Cópia rasa
lista_original = [1, 2, 3]
copia = lista_original[:]
copia.append(4)
print(lista_original)  # [1, 2, 3]
print(copia)  # [1, 2, 3, 4]