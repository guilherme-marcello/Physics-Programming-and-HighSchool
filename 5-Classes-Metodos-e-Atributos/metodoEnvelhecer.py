class Pessoa:
    
    def __init__(self,name,age):
        self.nome = name
        self.idade = age
    
    def apresentar(self):
        print("Olá, o meu nome é "+ self.nome + " e a minha idade é " + str(self.idade))

    def envelhecer(self):
        self.idade += 1

jonas = Pessoa("Jonas",5)

jonas.apresentar()

jonas.envelhecer()

jonas.apresentar()

