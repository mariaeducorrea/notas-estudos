'''
Em Python, tratamento de erros é uma parte importante para garantir que seu código seja mais robusto e não quebre durante a execução. Isso é feito utilizando blocos try, except, mas existem outros comandos relacionados a isso, como else, finally e até mesmo a geração de erros com raise.
'''

#try:
    #o código que pode gerar erro
#except:
    #o código para tratar o erro

try:
    num = int(input("Digite um número: "))
    print(f"O número digitado é {num}")
except ValueError:
    print("Erro! Você não digitou um número válido.")


#else 
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro! Não é um número.")
else:
    print(f"Você digitou o número {numero} com sucesso.")


#finally
try:
    arquivo = open("exemplo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
else:
    print("Conteúdo do arquivo:", conteudo)
finally:
    print("Bloco finally executado.")
    arquivo.close()  # Garantindo que o arquivo seja fechado


#Gerando Erros com raise
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida!")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(e)



# Exemplo usando todas:

try:                   #tenta executar o código que pode gerar erros (conversão de entrada para inteiro e divisão).
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:    #captura e lida com exceções específicas
    print("Você não digitou um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:                 #é executado somente se nenhum erro ocorrer.
    print(f"O resultado é: {resultado}")
finally:              #é executado sempre, independentemente de haver erro ou não, útil para liberar recursos.
    print("Operação finalizada.")


''''
Tipos de exceções 

- ValueError: Quando uma função recebe um argumento de tipo correto, mas com valor inadequado (ex.: tentando converter uma string não numérica em um número).
- ZeroDivisionError: Quando ocorre uma divisão por zero.
- TypeError: Quando uma operação ou função é aplicada a um objeto de tipo incorreto.
- IndexError: Quando se tenta acessar um índice de uma lista ou sequência que não existe.
- FileNotFoundError: Quando um arquivo não pode ser encontrado no sistema.
- KeyError: Quando se tenta acessar uma chave inexistente em um dicionário.
'''

'''
Quando Usar o Tratamento de Erros?
Use o tratamento de exceções quando você sabe que uma operação pode falhar de forma previsível, e você deseja tratá-la de maneira controlada. Por exemplo, ao tentar acessar um arquivo, ao fazer uma conversão de tipo, ou ao dividir números.

Quando Não Usar o Tratamento de Erros?
Não é recomendado usar o tratamento de exceções em casos onde você pode prever facilmente o erro e resolvê-lo de outra maneira. Em vez disso, você deve tratar a causa do erro diretamente.

'''

