'''
As Funções de Ordem Superior são aquelas que podem:

Receber uma ou mais funções como argumento(s).
Retornar uma função como resultado.

Portanto, toda função de ordem superior é uma função que usa funções como entrada ou saída, ou seja, uma função que opera sobre outras funções.
'''

# Funções que recebem outras funções como argumentos:
def aplicar(func, lista):
    return [func(x) for x in lista]

def quadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4]
#Aqui, a função aplicar é uma função de ordem superior que recebe a função quadrado e a lista numeros. A função quadrado é aplicada a cada elemento da lista.
resultado = aplicar(quadrado, numeros)
print(resultado)



# Funções que retornam outras funções:
def multiplicador(fator):
    def multiplicar(n):
        return n * fator
    return multiplicar

# Criando uma função que multiplica por 3
multiplica_por_3 = multiplicador(3)
#A função multiplicador recebe um argumento fator e retorna a função multiplicar, que usa esse fator para multiplicar um número. Aqui, multiplica_por_3 é uma função criada dinamicamente que multiplica qualquer número por 3.
# Usando a nova função
print(multiplica_por_3(5))  # 5 * 3 = 15