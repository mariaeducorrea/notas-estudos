'''
Módulos padrão do python (import, from, as , *)

'''

#IMPORT
# A palavra-chave import é usada para importar um módulo inteiro. Quando você importa um módulo dessa maneira, você precisa usar o nome do módulo para acessar suas funções e variáveis.
#sintaxe: import nome_do_modulo
# exemplo: import math


#FROM
#A palavra-chave from permite importar uma parte específica (geralmente uma função ou classe) de um módulo
#sintaxe: from nome_do_modulo import nome_da_funcao
#exemplo: import math import spwd


#AS
#Você pode usar a palavra-chave as para importar um módulo ou uma função com um nome alternativo (um alias).
#sintaxe: import nome_do_modulo as alias
#exemplo: import math as m 


# *
#A palavra-chave * (asterisco) importa tudo de um módulo, ou seja, todas as suas funções, classes e variáveis se tornam diretamente acessíveis no seu código.
#sintaxe: from nome_do_modulo import *
#exemplo: from math import *


'''
Existem diferentes tipos de módulos que você pode usar ou criar:

Módulos padrão (embutidos): Módulos que vêm junto com a instalação do Python.
Módulos externos: Módulos que você instala usando ferramentas como pip.
Módulos personalizados: Módulos criados por você, que podem ser reutilizados em seus projetos.
'''

# Embutidos
# math, os, sys...
import math 

print(math.sqrt(16))

# Externos 
# pip install pandas 

# Personalizados
# Crie um arquivo .py com o nome do módulo. Por exemplo, crie um arquivo chamado meu_modulo.py: