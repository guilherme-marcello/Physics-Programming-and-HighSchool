class Pessoa:
    def __init__(self,name,age):
        self.nome = name
        self.idade = age

jonas = Pessoa("Jonas",5)
print(jonas.nome)
print(jonas.idade)
print(type(jonas))
