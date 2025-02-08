"""
List comprehension é uma forma concisa e poderosa de criar listas em Python. Ela permite gerar listas a partir de iteráveis, aplicando condições ou transformações, em uma única linha de código.

nova_lista = [expressão for item in iterável if condição]

expressão: O que será adicionado à nova lista.
for item in iterável: Itera sobre o iterável.
if condição (opcional): Filtra os itens com base em uma condição

"""

# Criar uma lista de números ao quadrado
numeros = [1,2,3,4,5,6,7,8,9,10]
quadrados = [i**2 for i in numeros]
print(quadrados)


# Filtrar números pares
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [i for i in numeros if i % 2 == 0]
print(pares)



# Criar combinações de dois iteráveis:
cores = ['vermelho', 'azul']
tamanhos = ['P', 'M', 'G']
combinacoes = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
print(combinacoes)

# Criar uma lista de tuplas
tuplas = [(x, x**2) for x in range(5)]
print(tuplas)  # Saída: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Converter todas as palavras de uma lista para maiúsculas:
palavras = ["python", "é", "legal"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)  # Saída: ['PYTHON', 'É', 'LEGAL']