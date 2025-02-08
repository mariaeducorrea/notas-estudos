'''
Generator Function
Uma função geradora é definida de maneira semelhante a uma função normal, mas em vez de usar a palavra-chave return para retornar um valor, ela usa a palavra-chave yield. O yield não apenas retorna um valor, mas também "pausa" a execução da função, permitindo que ela continue de onde parou quando chamada novamente (quando a próxima iteração for solicitada). 

return: Termina a execução da função e envia o valor de volta para o chamador.
yield: Pausa a execução da função, retira um valor e pode retomar a execução quando o valor for solicitado novamente.

'''

#exemplo
def generator(n=0):
    yield 1 #pausar
    print("...")
    yield 2  #pausar
    print("...")
    yield 3   
    print("fim")

gen = generator(n=0)
for n in gen:
    print(gen)


#com while
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(n=0, maximum=10)
for n in gen:
    print(n)




# yield from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()





