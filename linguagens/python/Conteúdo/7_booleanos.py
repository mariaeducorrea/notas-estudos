# Valore booleanos

a = True
b = False

print(type(a))
print(type(b))

# Operadores lógicos 
#and
print("and")
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print()

#or
print("or")
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print()

#not
print("not")
print(not True)
print(not False)

#Comparaçoes booleanas
a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False


#__________________________________

#Exemplos de uso
a = 10
b = 5

# Condicional com `and`
if a > b and b < 10:
    print("Condição AND satisfeita")  

# Condicional com `or`
if a < b or b < 10:
    print("Condição OR satisfeita")  

if not (a == b):
    print("Condição not satisfeita") 
