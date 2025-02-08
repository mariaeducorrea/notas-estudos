# Criando uma tupla
tupla1 = (1, 2, 3, 4)
tupla2 = 'a', 'b', 'c', 'd'

# Tupla vazia
tupla_vazia = ()
print(tupla_vazia)

# Tupla com um único elemento (vírgula necessária)
tupla_unica = (5,)
print(tupla_unica)

# Acessando elementos
print(tupla1[0])  
print(tupla1[-2])  # Quando negativo começa indice de trás para frete

# Fatiamento
tupla_fat = ()
print(tupla2[1:3])  # (2, 3)
print(tupla2[:2])   # (1, 2)
print(tupla2[::2])  # (1, 3)

# Integração com loops
tupla_loop = 'Maria', 'João', 'Micael', 'Ana'
for item in tupla_loop:
    print(f'Esse é {item}')

# Concatenação
nova_tupla = tupla1 + tupla2
print(nova_tupla)  # (1, 2, 3, 4, 'a', 'b', 'c', 'd')

# Repetição
tupla_repetida = tupla1 * 2
print(tupla_repetida)  # (1, 2, 3, 4, 1, 2, 3, 4)

# Comprimento da tupla
print(len(tupla1))  # 4

# Contagem de elementos
print(tupla1.count(2))  # 1

# Índice de um elemento
print(tupla1.index(3))  # 2

# Converta lista em tupla
lista = [5, 6, 7]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (5, 6, 7)

# Desempacotamento
a, b, c, d = tupla2
print(a, b, c, d)  # 'a' 'b' 'c' 'd'

# Ignorando elementos com "_"
a, _, c, _ = tupla2