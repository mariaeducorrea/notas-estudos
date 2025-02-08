# break
# Interrompe a execução de um loop prematuramente. Pode ser usado em qualquer loop.
# Em uma função ele interrompe o loop mas não sai da função, o codigo fora do loop executa normal

# continue
#Faz o loop pular para a próxima iteração, pulando o restante do código dentro do loop para aquela iteração.

# return
#Só pode ser usado dentro de uma função. O return é usado para sair imediatamente de uma função, retornando um valor ou apenas saindo, se não houver valor a ser retornado. 
# Ele encerra o loop e sai imediatamente na função mesmo tendo mais blocos na função para executar.

#yield
#Usado para criar geradores. Ele "pausa" a execução da função e retorna um valor, mas a função pode ser retomada de onde parou.

# for

#for + break
for i in range(10):
    if i == 5:
        print("Encontrado 5, saindo do loop com 'break'.")
        break
    print(i)

def for_break():
    for i in range(10):
        if i == 5:
            print("Encontrado 5, saindo do loop com 'break'.")
            break  # Interrompe o loop quando i for 5
        print(i)

for_break()



#for + continue 
for i in range(10):
    if i % 2 == 0:
        continue  # Pula a iteração quando i é par
    print(f"Ímpar: {i}")

def for_continue():
    for i in range(10):
        if i % 2 == 0:
            continue  # Pula a iteração quando i é par
        print(f"Ímpar: {i}")

for_continue()


#for + return
def for_return():
    for i in range(10):
        if i == 5:
            return f"Função encerrada no número {i}"  # Retorna e sai da função
        print(i)
    return "Nenhum número foi encontrado."

resultado = for_return()
print(resultado)


#for + yield
def for_yield():
    for i in range(5):
        yield i  # Retorna um valor e pausa a execução da função

gerador = for_yield()
for valor in gerador:
    print(f"Valor gerado: {valor}")




# while 

#while + break
i = 0
while i < 10:
    if i == 5:
        print("Encontrado 5, saindo do loop com 'break'.")
        break  # Interrompe o loop quando i for 5
    print(i)
    i += 1

def while_break():
    i = 0
    while i < 10:
        if i == 5:
            print("Encontrado 5, saindo do loop com 'break'.")
            break  # Interrompe o loop quando i for 5
        print(i)
        i += 1

while_break()


#while + continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Pula a iteração quando i for par
    print(f"Ímpar: {i}")

def while_continue():
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue  # Pula a iteração quando i for par
        print(f"Ímpar: {i}")

while_continue()


#while + return 
def while_return():
    i = 0
    while i < 10:
        if i == 5:
            return f"Função encerrada no número {i}"  # Retorna e sai da função
        print(i)
        i += 1

resultado = while_return()
print(resultado)


# while + yeld
def while_yield():
    i = 0
    while i < 5:
        yield i  # Retorna um valor e pausa a execução da função
        i += 1

gerador = while_yield()
for valor in gerador:
    print(f"Valor gerado: {valor}")