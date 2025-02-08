# Manipulaçao de string

# Definindo strings
str1 = "Olá"
str2 = "Mundo"
texto = "Python é incrível!"


# Concatenação
resultado = str1 + " " + str2  # "Olá Mundo"
print(resultado)

# Repetição
repetido = str1 * 3  # "OláOláOlá"
print(repetido)

# Acessar caracteres - Indexação
print(str2[0])   # "P"
print(str2[-1])  # "!"

# Fatiamento (substring) - Fatiamento
print(texto[0:6])     # "Python"
print(texto[7:])      # "é incrível!"
print(texto[:6])      # "Python"
print(texto[::2])     # "Pto énicvl"


# Modificação de Texto
texto = " aprendizado é constante "
print(texto.upper())       # " APRENDIZADO É CONSTANTE "
print(texto.lower())       # " aprendizado é constante "
print(texto.strip())       # Remove espaços extras: "aprendizado é constante"
print(texto.replace("aprendizado", "estudo"))  # " estudo é constante "
print(texto.title())       # " Aprendizado É Constante "
print(texto.capitalize())  # " aprendizado é constante "

# Verificação
texto = "Python3"

print(texto.isalpha())    # False (contém números)
print(texto.isdigit())    # False (não é só número)
print(texto.isalnum())    # True (letras e números)
print(texto.startswith("Py"))  # True
print(texto.endswith("3"))     # True

# Divisão em lista
frase = "Aprender Python é divertido"
palavras = frase.split()  # ["Aprender", "Python", "é", "divertido"]
print(palavras)

# Divisão por delimitador
csv = "nome,idade,cidade"
dados = csv.split(",")    # ["nome", "idade", "cidade"]
print(dados)

# Junção de lista em string
juncao = " ".join(palavras)  # "Aprender Python é divertido"
print(juncao)

#Formatação de Strings
nome = "Maria"
idade = 25
# Formatação com f-strings (recomendado)
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Método format()
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Antigo (%)
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))