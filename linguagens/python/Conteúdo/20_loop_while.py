"""
Os loops são estruturas que permitem que um bloco de código seja executado repetidamente enquanto uma condição for verdadeira. 
- Loop while: Executa um bloco de código enquanto uma condição for verdadeira.
- Loop for: Itera sobre uma sequência (como uma lista, string, ou intervalo) e executa um bloco de código para cada item dessa sequência.
"""

# WHILE

i = 0
while i < 5:
    print(i)
    i += 1

# Break
# Break serve para interromper um loop
i = 5
while True:       #loop infinito
    if i == 9:
        break # Interrompe o loop quando i for igual a 3
    print(i)
    i += 1

# Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue # pula o código abaixo quando i for igual a 3
    print(i)
    
# While aninhado
i = 0   #declara variavel da while "pai"
while i < 3:
    j = 0   #declara a variavel da while "filho" 
    while j < 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# While contador
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# While com string
texto = "python"
print(len(texto))
i = 0
while i < len(texto):
     print(texto[i])
     i += 1

# While com tuplas
frutas = ("maça","laranja","abacaxi")
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# While com list
nomes = ["Maria","Ana","lucas"]
i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1