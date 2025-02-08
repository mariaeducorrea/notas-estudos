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