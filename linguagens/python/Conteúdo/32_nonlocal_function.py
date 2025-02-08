'''
Variavel livre
Uma variável livre é uma variável que não é local para a função em que está sendo usada e também não é global. Em outras palavras, é uma variável que é referenciada dentro de uma função, mas que não é declarada nem local (ou seja, não existe dentro daquela função).
'''
x = 10

def funcao():
    print(x)

funcao()


'''
Variavel nonlocal
O nonlocal é uma palavra-chave em Python que permite modificar variáveis em um escopo não local, ou seja, em um escopo de uma função que não é nem o escopo global nem o local da função que está sendo executada. Ele é especialmente útil quando se trabalha com funções aninhadas e você precisa modificar uma variável que está em um escopo mais interno, mas não no escopo local.
'''
def funcao_externa():
    x=10

    def funcao_interna():
        nonlocal x  #se refere a variavel x da funcao_externa
        x=20    #modifica variavel x no escopo da funcao externa

    
    funcao_interna()
    print(x)

funcao_externa()




'''
globals
O globals() é uma função interna que retorna o dicionário global do módulo atual. Ele contém todas as variáveis globais do seu código.
'''

x=10

def funcao_interna():
    
    globals()['x'] = 20   
    

funcao_interna()
print(x)
