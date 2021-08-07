class Pessoa:
    
    def __init__(self,name,age):
        self.nome = name
        self.idade = age
    
    def apresentar(self):
        print("Olá, o meu nome é "+ self.nome + " e a minha idade é " + str(self.idade))

jonas = Pessoa("Jonas",5)

jonas.apresentar()

