"""
as funções dir(), hasattr() e getattr() são usadas principalmente para interagir com os atributos e métodos de objetos dinamicamente. Elas permitem verificar e acessar informações sobre os objetos em tempo de execução, o que pode ser útil quando estamos trabalhando com introspecção, ou seja, examinando ou modificando a estrutura de um objeto enquanto o código está sendo executado.
"""


# dir - retorna lista de todos os atributos e métodos de um objeto
string = "Maria"

print(dir(string))


#hasattr - verifica se objeto tem um atributo/metodos
#A função hasattr() é usada para verificar se um objeto possui um atributo específico. Ela retorna True se o objeto tiver o atributo e False caso contrário.
minha_lista = [1, 2, 3]

# Verificando se o objeto lista tem o atributo 'append'
print(hasattr(minha_lista, 'append'))  # Saída: True

# Verificando se o objeto lista tem o atributo 'remove'
print(hasattr(minha_lista, 'remove'))  # Saída: True


#getattr - Obtém o Valor de um Atributo
#A função getattr() é usada para obter o valor de um atributo de um objeto. Se o atributo não existir, você pode definir um valor padrão para retornar (caso contrário, ocorrerá um erro AttributeError).
# Criando uma lista
minha_lista = [1, 2, 3]

# Usando getattr para acessar o método 'append' da lista
append_method = getattr(minha_lista, 'append', None)
if append_method:
    append_method(4)  # Adiciona 4 à lista
print(minha_lista)  
