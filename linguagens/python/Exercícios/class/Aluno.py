# Crie uma classe Aluno com os atributos nome, matricula e notas (uma lista de notas).
# Implemente métodos para adicionar uma nova nota e calcular a média das notas.
# Implemente um método para verificar se o aluno está aprovado (média >= 7).

class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self):
        try:
            nota = float(input("Digite a nota: "))
            self.notas.append(nota)
        except ValueError:
            print("Valor inválido! Digite a nota corretamente.")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            print(f"Aluno/a {self.nome} está aprovado/a com média {media:.2f}")
        else:
            print(f'Aluno/a {self.nome} está reprovada/a com média {media:.2f}')
    

aluno1 = Aluno('Maria','12345')

aluno1.adicionar_nota()
aluno1.adicionar_nota()
aluno1.adicionar_nota()
aluno1.calcular_media()
aluno1.verificar_aprovacao()
