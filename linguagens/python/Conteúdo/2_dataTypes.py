"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

'''
->  NÚMERICO
int: Números inteiros, positivos ou negativos, sem decimais.
float: Números de ponto flutuante (decimais).
complex: Números complexos com parte real e imaginária.
    -  Existem regras específicas para a criação de números complexos em Python!
        > Uso do j: É obrigatório para denotar a parte imaginária.
        > Partes Real e Imaginária: Ambas podem ser números inteiros ou de ponto flutuante. (z = 1.5 + 2.3j)
        > Somente a Parte Imaginária: Quando apenas a parte imaginária existe, a parte real é assumida como 0.
        > Representação Interna: Os números complexos são armazenados como complex(real, imag) internamente. (z = complex(1, 2)  # Equivalente a 1 + 2j)
'''
x = 10      #int
y = 10.5    #float
z = 1 + 2j  #complex

print('Tipos Númericos')
print(type(x))
print(type(y))
print(type(z))
print('Tipos Númericos print')
print(x)
print(y)
print(z)
print()
#____________________________________________________________________________________

'''
-> TEXTO
str: Cadeia de caracteres (strings), usada para representar texto.
'''
texto = "Olá mundo!"
letra = 'P'

print('Tipos String')
print(type(texto))
print(type(letra))
print('Tipos String print')
print(texto)
print(letra)
print()

#____________________________________________________________________________________

'''
-> BOOLEANO
bool: Representa valores lógicos, True ou False.
'''
on = True
off = False
a = 10
b = 10
c = 5

print('Tipos Booleano')
print(type(on))
print(type(off))
print('Tipos Booleano print')
print(on)
print(off)
print()

#____________________________________________________________________________________

'''
-> SEQUÊNCIA
list: Lista mutável, pode conter diferentes tipos de dados.
tuple: Tupla imutável, pode conter diferentes tipos de dados.
range: Intervalo de números.
'''
lista = [1,'João','abc',45,'Maria']
tuplas = (1,'João','abc',45,'Maria')
intervalo = range(5) 

print('Tipos Sequencia')
print(type(lista))
print(type(tuplas))
print(type(intervalo))
print('Tipos Sequencia print')
print(lista)
print(tuplas)
print(list(intervalo))
print()

#____________________________________________________________________________________

''''
-> MAPEAMENTO
dict: Dicionário, que armazena pares de chave-valor.
'''
dados = {
    "nome":"Maria",
    "idade":23,
    "cidade":"POA"
}

print('Tipo Mapeamento')
print(type(dados))
print('Tipo Mapeamento print')
print(dados)
print()


#____________________________________________________________________________________

'''
-> CONJUNTOS
set: Conjunto não ordenado e sem duplicatas.
frozenset: Conjunto imutável.
'''
conjunto = {1,2,3,4}

print('Tipo Conjunto')
print(type(conjunto))
print('Tipo Conjunto print')
print(conjunto)
print()

#____________________________________________________________________________________

'''
-> BINÁRIOS
bytes: Sequência imutável de valores de bytes.
bytearray: Sequência mutável de valores de bytes.
memoryview: Permite acessar a memória de outro objeto sem copiá-lo.
'''
b = b"python"
ba = bytearray(4)
mv = memoryview(b"python")


print('Tipo Binário')
print(type(b))
print(type(ba))
print(type(mv))
print('Tipo Binário print')
print(b)
print(ba)
print(mv)

#____________________________________________________________________________________


# BINÁRIO
#bytes
#É usada para armazenar dados binários, como texto codificado ou dados brutos. 
b = b"hello"
print(b)  

#bytearray
#Uma versão mutável de bytes. Permite modificar bytes individuais.
ba = bytearray([65, 66, 67])
ba[0] = 90  
print(ba)  

#memoryview
#Um objeto de visualização que permite acessar os dados de um objeto sem copiá-los. Funciona para objetos que suportam o protocolo de buffer, como bytes ou bytearray.
mv = memoryview(b"hello")
print(mv[0])  

#____________________________________________________________________________________

# NONE

#O tipo do objeto None. None é usado para representar a ausência de valor ou um valor nulo.
x = None
print(type(x)) 

