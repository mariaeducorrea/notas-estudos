'''
Funções com um número variável de argumentos permitem que você passe um número indefinido de argumentos para uma função. Isso é especialmente útil quando você não sabe quantos parâmetros a função precisará, ou quando deseja uma maior flexibilidade ao definir funções.

Há duas maneiras principais de definir funções que aceitam um número variável de argumentos:
- Argumentos posicionais variáveis (*args).
- Argumentos nomeados variáveis (**kwargs).
'''

# args = Empacota todos os argumentos adicionais em uma tupla. Isso significa que você pode acessar os argumentos passados com base na posição.

# O *args coleta os argumentos passados da linha 15 e 16 e os armazena como uma tupla. A função então soma todos os elementos dessa tupla.

def soma(*args):
    return sum(args)

print(soma(1,2,3))
print(soma(5,6,4,8,7,8,10))


# kwargs =  empacota todos os argumentos nomeados em um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores passados.

def imprime_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprime_informacoes(nome="João",idade=25, cidade="SP")


# *args + **kwargs
def apresenta_pessoa(nome, *args, **kwargs):
    print(f"Nome: {nome}")
    print("Outros detalhes:")
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função
apresenta_pessoa("Ana", 25, "Programadora", cidade="Rio de Janeiro", hobby="Futebol")