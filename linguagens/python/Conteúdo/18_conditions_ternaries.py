
# CONDICIONAIS TERNÁRIAS

# simplificar expressões condicionais em uma única linha de código

# bloco 1
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)  

# bloco 2
numero = 5
resultado = "Par" if numero % 2 == 0 else "Ímpar"
print(resultado)

#bloco 3 
nota = 7
if nota >= 6:
    status = "Aprovado"
else:
    status = "Reprovado"
print(status)  # Saída: Aprovado

# bloco 4
idade = 20
categoria = "Criança" if idade < 12 else "Adolescente" if idade < 18 else "Adulto"
print(categoria) 