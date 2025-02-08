"""
> Função:
Uma função em Python é um bloco de código que é projetado para realizar uma tarefa específica.
Elas são definidas usando a palavra-chave def, seguida do nome da função e, opcionalmente, de parâmetros.

def nome_da_função(parametro1,parametro2)
    #corpo da função = o que ela irá executar
    resultado = parametro1 + parametro2
    return resultado

"""

# Definindo uma função:
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()


# Função com parametros:
def bye(nome):
    print(f"Volte sempre {nome}!")

bye("Maria")


# Função com retorno:
#Funções também podem retornar um valor, o que significa que o resultado da função pode ser usado em outras partes do código.
def soma(a,b): 
    return a + b

resultado = soma(10,5)
print(resultado)

# Função com multiplos retornos:
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

resultado = operacoes(3, 5)
print(resultado)


# Parametros opcioanis:
def saudacao(nome="Visitante", idade=30):
    print(f"Olá {nome}! Você tem {idade} anos.")
              
saudacao()  #irá imprimir valor padrao
saudacao("Ana", 35)     #usa valores determinados


