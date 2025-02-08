# Herança múltipla é um conceito onde uma classe filha pode herdar características (atributos e métodos) de mais de uma classe pai. Ou seja, uma classe pode ser derivada de várias classes, e herdar comportamentos e propriedades de todas essas classes simultaneamente.

class A():
    def falar(self):
        print('A fala.')

class B():
    def falar(self):
        print('B fala.')

class C(A, B):
    pass


c = C()

c.falar()
c.falar()


'''
O Python utiliza um mecanismo chamado MRO para determinar qual classe deve ser usada para um determinado método ou atributo. Quando você cria uma classe como class C(A, B), o Python gera uma ordem de resolução de métodos para essa classe.
'''
print(C.mro())
