#Peça um número ao usuário e informe se é par ou ímpar.

def par_impar():
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par!")
        else: 
            print(f"O número {numero} é impar!")
    except ValueError:
        print("Valor inválido! Digite números inteiros.")

par_impar()