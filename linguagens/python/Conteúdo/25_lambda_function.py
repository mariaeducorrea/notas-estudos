'''
Funções lambda são funções pequenas e simples, criadas sem a necessidade de usar a palavra-chave def. Elas são frequentemente usadas em operações curtas e temporárias.

nome_funcao = lambda argumento1, argumento2: expressão
'''

# Exemplo
soma = lambda a, b: a + b 
print(soma(5,6))

# Usando map
#O map() aplica uma função a cada item de um iterável (como uma lista) e retorna um novo iterável com os resultados.
lista = [1,3,4,5]

quadrado = map(lambda x: x**2, lista)
print(list(quadrado))


# Usando filter
#O filter() filtra os elementos de um iterável com base em uma condição (função que retorna True ou False).
numeros = [1,2,3,4,5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))


# Usando sorted
#A função sorted() ordena elementos. Você pode usar lambda para definir a chave de ordenação.
tuplas = [(5,2),(1,3),(4,6)]
ordenando = sorted(tuplas, key=lambda x: x[0])
print(ordenando)

