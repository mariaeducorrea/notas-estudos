# Relações entre classes  - A relação entre as classes são diferenciadas pela "força de dependência" entre elas.


#Associação: uma classe usa outra sem que haja um dependencia direta,  o objeto de uma classe pode estar em outra classe sem a mesma possuir esse objeto/atributo
class Motor:
    def ligar(self):
        print("ligando motor! Aguarde...")

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def ligar_motor(self, motor : Motor ):
        motor.ligar()
        print(f"{self.modelo} está pronto para rodar.")

motor = Motor()
carro = Carro('Sedan')

carro.ligar_motor(motor)



#Agregação: uma classe possui outra, mas os objetos podem existir separadamente
class Departamento:
    def __init__(self, nome):
        self.nome = nome


class Empresa:
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.departamentos = []

    def adicionar_departamento(self, departamento : Departamento):
        self.departamentos.append(departamento)

    def listar(self):
        print(f"Departamentos da empres {self.nome_empresa}")
        for departamento in self.departamentos:
            print(departamento.nome)

empresa = Empresa('Techhouse')
dep1 = Departamento('RH')
dep2 = Departamento('TI')


empresa.adicionar_departamento(dep1)
empresa.adicionar_departamento(dep2)
empresa.listar()



#Composição: Uma classe possui outra, e os objetos são fortemente dependentes. Se o objeto principal for destruído, o objeto dependente também será.
class Processador:
    def __init__(self, modelo, seila):
        self.modelo = modelo
        self.seila = seila

class Computador:
    def __init__(self, pc, procesador_modelo, seila):
        self.pc = pc
        self.processador = Processador(procesador_modelo, seila)

    def infos(self):
        print(f"{self.pc} com processador {self.processador.modelo} e de cor {self.processador.seila}")

proc = Computador('lenovo','Ryzen7','preto')
proc.infos()


#Hernaça: Uma classe herda atributos e métodos de outra.
class Animal:
    def falar(self):
        print("Som qualquer.")

class Cachorro:
    def falar(Animal):
        print("auau")

class Gato:
    def falar(Animal):
        print("miau")

class Pessoa:
    def falar(Animal):
        print("kkkkk")

dog = Cachorro()
cat = Gato()
people = Pessoa()

dog.falar()
cat.falar()
people.falar()