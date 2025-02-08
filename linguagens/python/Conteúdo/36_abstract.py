from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def som(self):
        pass

    @abstractmethod
    def brinca_como(self):
        pass


class Cachorro(Animal):
    def som(self):
        return "au au!"
    
    def brinca_como(self):
        return f"{self.nome} busca graveto."

    
class Gato(Animal):
    def som(self):
        return "miau miau!"
    
    def brinca_como(self, acordado=True):
        if not acordado:
            return f"{self.nome} não está acordado/a para dormir."
        
        return f"{self.nome} brinca com rato de brinquedo."
    


dog = Cachorro(nome='felix')
cat = Gato(nome='mica')

print(dog.som())
print(dog.brinca_como())

print(cat.som())
print(cat.brinca_como(acordado=True))
print(cat.brinca_como(acordado=False))