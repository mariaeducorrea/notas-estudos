from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
# Abstração: Criamos uma classe abstrata que define um modelo para as subclasses usarem.
    @abstractmethod
    def area(self):
        pass        #Nos métodos abstratos não implementamos a lógica. Apenas definimos que todas as subclasses devem implementá-lo, pois isso é usado o pass.


# Herança : Criamos classe que herda da classe abstrata, são obrigadas a implementar o método 'area'
class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    

# Polimorfismo: Criamos uma função que aceita qualquer objeto que siga o contrato da classe 'FormaGeometrica'. Como todas as subclasses implementam 'area', podemos chamá-la sem precisar saber o tipo da forma.
def calcular(forma):
    print(f'Área da forma: {forma.area()}')


quadrado = Quadrado(4)
circulo = Circulo(2)

calcular(quadrado)
calcular(circulo)