
#Peça três números ao usuário e exiba o maior deles.

def maior_numero():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        n3 = float(input("Digite o terceiro número: "))
        maior = max(n1, n2, n3)
        print(f"O maior número é {maior}")
    except ValueError:
        print("Digite um valor válido!")
        
maior_numero()
