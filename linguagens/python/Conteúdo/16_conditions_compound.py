
# CONDICIONAIS COMPOSTAS

# bloco 1
idade = 25
renda = 3000

if idade >= 18: # primeira condicao
    if renda >=2000:
        print("Você atende a todos os requisitos.")
    else:
        print("Você precisa de uma renda maior.")
else:
    print("Você não atende a idade necessária!")

# bloco 2
nota =  8.5
frequencia = 90

if nota > 7:
    if frequencia >= 75:
        print("Aprovado.")
    else:
        print("Reprovando por frequencia.")
else: 
    if frequencia < 75:
        print("Reprovado por nota e frequencia.")
    else:
        print("Reprovado por nota.")
