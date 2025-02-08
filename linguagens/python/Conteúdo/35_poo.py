# Programação Orientada a Objetos (POO) - Estrutura Base

'''Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos e suas interações.'''

class Pessoa:
    """Classe que representa uma pessoa, e que contém atributos e métodos para definir o comportamento de um objeto pessoa."""

    #Método contrutor(__init__): Inicializa os atributos do objeto
    def __init__(self, nome, idade):
        #Atributos, propriedades do obejto.
        self.nome = nome
        self.idade = idade


    #Método (Função dentro da classe): Representa uma ação da classe
    def apresentar(self):
        """"Método para apresentar a pessoa"""
        return f"Olá! Meu nome é {self.nome} e eu tenho {self.idade} anos."
    
    #Método de modificação(altera valores dos atributos)
    def envelhecer(self, anos=1):
        self.idade += anos
        return f"{self.nome} agora tem {self.idade} anos."
    
    #Método estático (Não precisa de atributos da instância)
    @staticmethod
    def mensagem():
        """Método que não usa atributos do obejto, apenas retorna mensagem."""
        return "Mensagem estática!"
    

#Criação de objeto (Instanciando a classe Pessoa)
pessoa1 = Pessoa("Carlos", 30)
pessoa2 = Pessoa("João", 25)

#Chamando métodos do objeto
print(pessoa1.apresentar())
print(pessoa2.apresentar())

#Modificando atributos com o método envelhecer 
print(pessoa1.envelhecer(10))

#Chamando um método estático
print(Pessoa.mensagem())
