# TIPOS NÚEMRICOS
print("TIPOS NÚEMRICOS")
print("> Operações aritméticas básicas")
a = 10
b = 5
print(a + b)  # soma
print(a - b)  # subtração
print(a * b)  # multiplicação
print(a ** b)  # multiplicação inteira
print(a / b)  # divisão
print(a // b)  # divisão inteira
print()
print("> Operações com números complexos.")
z1 = 1 + 2j
z2 = 2 - 3j
print(z1 + z2)  # soma
print(z1 * z2)  # multiplicação
print(z1.real)  # acesso a parte real
print(z1.imag)  # acesso a parte imaginária
print()
print("> Arredondamento e conversões.")
z = 10.6789
print(round(z, 2))  # 10.68 (arredondar)
print(int(z))       # 10 (converter para inteiro)
print(float(z))     # 10.0 (converter para float)
print()


print("________________________________________________________________________________")

# TIPOS TEXTO
print("TIPO TEXTO")
print("> Concatenar e repetir strings")
nome = "João"
sobrenome = "Silva"
print(nome + " " + sobrenome)  
print(nome * 3) 
print()
print("> Métodos de manipulação")
texto = "Python"
print(texto.upper())  # PYTHON
print(texto.lower())  # python
print(texto.replace("P", "J"))  # Jython
print(texto.split("t"))  # ['Py', 'hon']
print()
print("> Acessar e fatiar strings")
print(texto[0])      # P
print(texto[1:4])    # yth
print(texto[-1])     # n
print()

print("________________________________________________________________________________")

# TIPOS BOOLEANDO
print("TIPO BOOLEANDO")
print("> Operações lógicas")
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
print()
print("________________________________________________________________________________")


# TIPO SEQUENCIA
print("TIPO SEQUENCIA")
print("> Adicionando, removendo e acessando elementos")
lista = [1, 2, 3]
lista.append(4)    # adicionadno
lista.insert(1, 5) # inserindo em um local especifico
lista.remove(2)    # removendo
print(lista[1])     # 5
print(lista[1:3])   # [5, 3]
print()
print("> Métodos de listas")
lista.sort()       # Ordena em ordem crescente
lista.reverse()    # Ordena em ordem decrescente
print(len(lista))  # Conta quant. elementos da lista
print()
print("> Acessar elementos (tuplas são imutáveis)")
tupla = (1, 2, 3)
print(tupla[1])    # 2
print()
print("> Gerar sequências de números")
for i in range(5):
    print(i)  

print("________________________________________________________________________________")

# TIPO MAPEAMENTO
print("TIPO MAPEAMENTO")
print("> Adicionar, remover e acessar valores")
dados = {"nome": "João", "idade":30}
dados["cidade"] = "POA"
print(dados)
print(dados["nome"])
del dados["idade"]
print(dados)
print()
print("> Métodos de dicionários")
print(dados.keys()) 
print(dados.values())
print(dados.items())

print("________________________________________________________________________________")


# CONJUNTOS
print("TIPO CONJUNTOS")
print("> Adicionando, removendo e operações matemáticas com conjuntos:")
conjunto = {1,2,3}
outro_conjunto={3,4,5}
conjunto.add(4)
conjunto.remove(2)
print(conjunto)
print(conjunto.union(outro_conjunto))
print(conjunto.intersection(outro_conjunto))
print(conjunto.difference(outro_conjunto))
print()
print("> Manipulação de frozenset:")
fs = frozenset([1,2,3]) 
#não é possível modificar 
print(fs)


print("________________________________________________________________________________")

# BINÃRIOS
print("TIPO BINÃRIOS")
print("> Criação e manipulação de bytes")
b = b"Python"
print(b[0])
print()
print("> Manipulação de bytearray")
ba = bytearray(4)
ba[0]=65
print(ba)
print()
print("> Acessar a memória de outros objetos")
mv = memoryview(b"Python")
print(mv[0])