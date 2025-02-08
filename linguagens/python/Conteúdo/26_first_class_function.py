'''
- First-Class Functions (Funções de Primeira Classe)
Em muitas linguagens de programação, funções são consideradas "cidadãos de segunda classe". Isso significa que elas não podem ser passadas como parâmetros, nem retornadas de outras funções. No entanto, em Python, as funções são consideradas de primeira classe. Ou seja, as funções podem:
Ser atribuídas a variáveis.
Ser passadas como argumentos para outras funções.
Ser retornadas de outras funções.
Em outras palavras, em Python, funções são tratadas da mesma forma que outros tipos de dados (como números, strings, listas, etc.).
'''


# Funções podem ser atribuídas a variáveis
def saudacao():
    return "Olá, mundo!"

minha_funcao = saudacao  # Atribuindo a função a uma variável
print(minha_funcao())  # Chamando a função através da variável


# Funções podem ser passadas como parâmetros:
def aplicar(func, x):
    return func(x)

def quadrado(n):
    return n ** 2

resultado = aplicar(quadrado, 5)
print(resultado)


# Funções podem ser retornadas de outras funções:
def saudacao_pessoal(nome):
    def saudacao():
        return f"Olá, {nome}!"
    return saudacao

minha_saudacao = saudacao_pessoal("João")  # Retorna a função saudacao personalizada
print(minha_saudacao())  # Chamando a função retornada
