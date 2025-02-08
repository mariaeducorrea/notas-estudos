# O polimorfismo permite que você trate diferentes objetos (mesmo que sejam de tipos diferentes) de maneira uniforme, chamando o mesmo método, mas com comportamentos específicos para cada tipo de objeto.

class Forma:
    def desenhar(self):
        pass


class Circulo(Forma):
    def desenhar(self):
        print("circulo")


class Quadrado(Forma):
    def desenhar(self):
        print("Quadrado")


formas = [Circulo(),Quadrado()]

for forma in formas:
    forma.desenhar()