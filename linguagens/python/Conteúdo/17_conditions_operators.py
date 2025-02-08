
# CONDICIONAIS MAIS OPERADORES RELACIONAIS

# bloco 1 = and
idade = 25
renda = 3000

if idade >= 18 and renda >= 2000:
    print("Você atende aos requisitos.")
else:
    print("Você não atende aos requisitos.")

# bloco 2 = or
idade = 16
tem_autorizacao = True

if idade >= 18 or tem_autorizacao:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")

# bloco 3 = not
tem_conexao = False

if not tem_conexao:
    print("Conexão indisponível.")
else:
    print("Conexão estabelecida.")

# bloco 4 = combinacoes de operadores
idade = 22
renda = 1500
estudante = True

if (idade >= 18 and renda >= 2000) or estudante:
    print("Você pode se inscrever.")
else:
    print("Você não pode se inscrever.")

# Prioridades de operadores 
'''
1.not
2.and
3.or
'''
condicao = True or False and not False
parte1 = not False  # = True
parte2 = False and True # = False
parte3 = True or False  # True

print(parte1)
print(parte2)
print(parte3)

#____________________________________________________________________________________

# CONDICIONAIS MAIS OPERADORES ARITMETICOS

# bloco 1
idade = 17
altura = 1.65
peso = 70
tem_autorizacao = False

# Condicional com vários operadores relacionais
if idade >= 18 and altura >= 1.50 and peso <= 100:
    print("Você pode participar da atividade!")
elif idade < 18 and tem_autorizacao and altura >= 1.50:
    print("Você pode participar com autorização!")
else:
    print("Você não atende aos requisitos para participar.")

# bloco 2
nota1 = 8
nota2 = 6
nota3 = 7
# Calcula a média
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado!")
elif 5 <= media < 7:
    print("Recuperação!")
else:
    print("Reprovado.")

# bloco 3
numero1 = 10
numero2 = 20

if numero1 > numero2:
    print("O número 1 é maior que o número 2.")
elif numero1 < numero2:
    print("O número 2 é maior que o número 1.")
else:
    print("Os números são iguais.")
