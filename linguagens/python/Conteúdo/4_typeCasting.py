# Typecasting = Typecasting é o processo de converter um tipo de dado em outro

#Tipos de Typecasting

# >>>> Implícito (Coerção de tipo):
    #Feito automaticamente pela linguagem de programação.
    #Ocorre quando tipos de dados menos precisos são convertidos para tipos mais precisos sem necessidade de intervenção do programador.

x = 10      #int
y = 2.5     #float
z = x + y   #x é convertido em float
print(z)


# >>>> Explícito (Typecasting manual):
    #Requer que o programador especifique a conversão.

# Conversão de string para inteiro
num_str = "100"
num_int = int(num_str)
print(num_int)
print(type(num_int))
print(num_int+50)

# Conversão deinteiro para float
num = 10
num_float = float(num)
print(num_float)
print(type(num_float))

#__________________________________________________________________________

#Métodos Comuns de Typecasting em Python

# str para int
str_int = int("10") 
print(type(str_int),'-',str_int)

# float para int
flt_int = int(5.8)
print(type(flt_int),'-',flt_int)

# str para float
str_flt = float("3.5")
print(type(str_flt),'-',str_flt)

# int para float
int_float = float(10)
print(type(int_float),'-',int_float)

# int para str
int_str = str(123)
print(type(int_str),'-',int_str)

# float pars str
float_str = str(3.14)
print(type(float_str),'-',float_str)

# str para list
string_list = list("abc")
print(type(string_list),'-',string_list)

# tupla para list
tuple_list = list((1, 2, 3))
print(type(tuple_list),'-',tuple_list)

# list para tupla
list_tuple = tuple([1, 2, 3])
print(type(list_tuple),'-',list_tuple)

# str para tupla
string_tuple = tuple("abc")
print(type(string_tuple),'-',string_tuple)

# list para conjunto
list_set = set([1, 2, 2, 3])
print(type(list_set),'-',list_set)

# str para conjunto
string_set = set("aabbcc")
print(type(string_set),'-',string_set)
