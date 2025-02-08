'''
- Expressões geradoras (generator expressions)
 são uma forma concisa e eficiente de criar geradores. Elas funcionam de maneira semelhante às compreensões de lista, mas em vez de gerar uma lista completa na memória, elas geram os valores sob demanda, o que pode ser muito mais eficiente em termos de uso de memória, especialmente quando se trabalha com grandes volumes de dados.

 Sintaxe:
( <expressão> for <item> in <iterável> if <condição> )

<expressão>: A expressão que será avaliada para cada item.
<item>: A variável que representa o item do iterável.
<iterável>: O objeto que você está iterando (como uma lista, tupla, etc.).
<condição>: (opcional) Uma condição para filtrar os itens

Diferença entre Compreensão de Lista e Expressão Geradora
compreensão de lista cria a lista inteira de uma vez, enquanto a expressão geradora cria os itens sob demanda, economizando memória.
'''

# Exemplo
quadrado = (x ** 2 for x in range(1,6))

for quadrado in quadrado:
    print(quadrado)


# Compreensão de Lista X Expressão Geradora
lista = [x ** 2 for x in range(1,6) ]
print(lista)

gerador = (x ** 2 for x in range(1,6))
for gerador in gerador:
    print(gerador)