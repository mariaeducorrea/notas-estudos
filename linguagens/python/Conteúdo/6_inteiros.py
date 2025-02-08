import math

# Operações matemáticas com int

# Operações básicas
a = 10
b = 3

print(a + b)  # Soma
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a // b) # Divisão inteira
print(a % b)  # Resto da divisão
print(a ** b) # Exponenciação

#Funções comuns com a biblioteca math
n = -15
x = 16

print(abs(n))           # Valor absoluto
print(math.sqrt(x))     # Raiz
print(math.pow(x, 3))   # Potência
print(math.gcd(36, 60)) # Máximo divisor comum
print(math.factorial(5)) # Fatorial


# Formatações
numero = 12345

# Formatação básica
print(f"Formatação simples: {numero}")

# Exibindo com zeros à esquerda
print(f"{numero:08}")  # "00012345"

# Separadores de milhar
print(f"{numero:,}")  # "12,345"

# Exibindo em base binária, octal ou hexadecimal
print(bin(numero))   # Binário: "0b11000000111001"
print(oct(numero))   # Octal: "0o30071"
print(hex(numero))   # Hexadecimal: "0x3039"


# Lista e inteiros
numeros = [1, 2, 3, 4, 5]

# Soma de todos os números
print(sum(numeros))  # 15

# Número máximo e mínimo
print(max(numeros))  # 5
print(min(numeros))  # 1