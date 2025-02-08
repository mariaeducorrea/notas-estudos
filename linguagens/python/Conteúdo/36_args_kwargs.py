
class animal:
    def __init__ (self, nome):
        self.nome = nome


    def acao(self, *args, **kwargs ):

        for alimento in args:
            print(f'{self.nome} esta comendo {alimento}')
        
        for chave, valor in kwargs.items():
            print(f"{self.nome} tem {chave}:{valor}")

    def executar(self, *args, **kwargs):
        print("Executando")
        self.acao(*args, **kwargs)
    
leao = animal(nome="Simba")

leao.executar("carne", "maça", "frago", idade=5, cor= "amarelo", filhos=2)