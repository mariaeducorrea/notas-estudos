# Crie uma classe chamada Carro que tenha os seguintes atributos: marca, modelo, ano, cor.
# Implemente métodos para mostrar as informações do carro e para "dirigir" (simulando a aceleração e frenagem).

class Carro():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def informacoes(self):
        return print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}')
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"Acelerando...Velocidade atual: {self.velocidade}")
    
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Desacelerando...Velocidade atual: {self.velocidade}")

c1 = Carro('Sandero','Stepway','2024','Preto')

c1.informacoes()
c1.acelerar(100)
c1.frear(40)