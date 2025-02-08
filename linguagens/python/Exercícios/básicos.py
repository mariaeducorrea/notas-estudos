#Peça um número ao usuário e informe se é par ou ímpar.
# def par_impar():
#     try:
#         numero = int(input("Digite um número: "))
#         if numero % 2 == 0:
#             print(f"O número {numero} é par!")
#         else: 
#             print(f"O número {numero} é impar!")
#     except ValueError:
#         print("Valor inválido! Digite números inteiros.")

# par_impar()

#Peça três números ao usuário e exiba o maior deles.
# def maior_numero():
#     try:
#         n1 = float(input("Digite o primeiro número: "))
#         n2 = float(input("Digite o segundo número: "))
#         n3 = float(input("Digite o terceiro número: "))
#         maior = max(n1, n2, n3)
#         print(f"O maior número é {maior}")
#     except ValueError:
#         print("Digite um valor válido!")
        
# maior_numero()


#Peça a idade do usuário e diga se ele é menor de idade, adulto ou idoso (menos de 18, entre 18-60, mais de 60).
def idade():
    idade = input("Digite sua idade: ")

    if idade.isdigit():
        idade_int = int(idade)
        if idade_int < 18:
            print("Você é de menor.")
        elif 18 <= idade_int < 60:
            print("Você é adulto.")
        elif  idade_int >= 60:
            print("Você é idoso.")
    else:
        print("Valor inválido! Digite apenas número.")

idade()