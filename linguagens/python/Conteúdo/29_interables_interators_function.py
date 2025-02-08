'''
- Interable - interáveis
Um objeto é considerado iterável se ele pode ser passado para a função iter(), que retorna um iterador para esse objeto. Ou seja, um iterável é algo que você pode usar com a função for para percorrer seus elementos.

Exemplos de iteráveis:
Listas (list)
Tuplas (tuple)
Dicionários (dict)
Conjuntos (set)
Strings (str)

'''
# identificar interável
# Exemplo com lista (que é iterável)
iterável = [1, 2, 3]

# Tentar obter um iterador usando a função iter()
iterador = iter(iterável)

print(iterador)  #<list_iterator object at 0x...>

# exemplo e interavel
lista = [1, 2, 3, 4]
for item in lista:
    print(item)
# Saída: 1, 2, 3, 4





'''
- Interators - interadores

Um iterador é um objeto que representa uma sequência de dados e permite que você acesse um elemento de cada vez. Ele é o "consumidor" de um iterável e é responsável por percorrer os itens do iterável. Um iterador deve implementar dois métodos principais:

__iter__(): Este método retorna o próprio iterador. Isso permite que o iterador seja usado com loops, como o for.
__next__(): Este método retorna o próximo item na sequência. Se não houver mais itens para retornar, ele levanta a exceção StopIteration, que é usada para indicar o fim da iteração.
'''
# Criando um iterador a partir de um iterável
iterável = [10, 20, 30]
iterador = iter(iterável)

# Usando o método __next__() para acessar os elementos
print(next(iterador))  # 10
print(next(iterador))  # 20
print(next(iterador))  # 30

