class Carro():
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True
        if self.ligado:  
            print('Carro ligado')
        return self.ligado
    
    def desligar(self):
        self.ligado = False
        if not self.ligado: 
            print("Carro desligado")
        return self.ligado
    
c1 = Carro()

c1.ligar()
c1.desligar()