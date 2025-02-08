#  Type hints (ou anotações de tipo) 
'''
Os type hints, ou “dicas de tipo”, foram introduzidos em Python para permitir que os desenvolvedores indiquem explicitamente os tipos de dados das variáveis e dos retornos de funções. Diferente de outras linguagens de programação, Python não obriga o uso de type hints, mas eles podem ser extremamente úteis para guiar quem está lendo o código.
'''

# Sintaxe básica em variáveis 
x: int = 10
y: float = 5.5
nome: str = 'maria'

print(f'{nome} : {type(nome)}')


# Sintaxe em funções
def somar(a: int,b:int) -> int:
    return a+ b

print(somar(4,5))

# Quando a função não retorna nda
def oi(nome:str) -> None:
    print(f'Olá {nome}!')

# Vantagem de usar 
'''
Legibilidade: Facilita a compreensão do código, especialmente em projetos grandes.
Manutenção: Ajuda a evitar erros comuns, como passar um tipo de dado inesperado para uma função.
Ferramentas de Desenvolvimento: IDEs como PyCharm e VS Code podem usar type hints para fornecer sugestões e detectar erros antes mesmo da execução do código.
'''

#list,tuples,dict
nome: list[str] = ['Lucia','Ana']
numeros: tuple[float] = (1,2,3)
compras: dict[str,float] = {
    'pão': 5.0,
    'arroz': 4.99,
    'Azeite': 8.50,
}


