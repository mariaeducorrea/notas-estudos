"""
Os loops são estruturas que permitem que um bloco de código seja executado repetidamente enquanto uma condição for verdadeira. 
- Loop while: Executa um bloco de código enquanto uma condição for verdadeira.
- Loop for: Itera sobre uma sequência (como uma lista, string, ou intervalo) e executa um bloco de código para cada item dessa sequência.
"""

# sintaxe
for i in range(5):
    print(i)


# list
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

#tuplas
numeros = (10, 20, 30)
for numero in numeros:
    print(numero)

#string
texto = "python"
for letra in texto:
    print(letra)

#dict
dados = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
for chave in dados:
    print(chave)

for valor in dados.values():
    print(valor)

for chave, valor in dados.items():
    print(f"{chave}: {valor}")


#for com range
for i in range(5):  # Gera os números de 0 a 4
    print(i)

#for com enumerate
frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

#Controle do Loop com break
for i in range(10):
    if i == 5:
        break
    print(i)

#Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)