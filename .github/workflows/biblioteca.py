
class Atleta():
    def __init__(self,peso,aposentado=False):
        self.aposentado=aposentado
        self.peso=peso
    def aposentar(self):
        print("o atleta está preste a  se aposentar")
    def aquecer(self):
        print(f"ele está preste a se aposentar,mas ainda esta jogando e está se aquecendo")

class Corredor(Atleta):


    def correr(self):
        if self.aposentado == False:
            self.aposentado = True
        if self.aposentado==True:
            print(f"o maratonista não está aposentado e está participando das maratonas")

        else:
            print(f"o maratonista está aposentado")
    def aquecer(self):
        print("O maratonista está aquecendo para a corrida nas cidades")

    def aposentar(self):
        print("O maratonista está fazendo a sua ultima corrida para se aposentar")
class Nadador(Atleta):
    def nadar(self):
        if self.aposentado==False:
            self.aposentado=True

        if self.aposentado==True:
            print("o  nadador não está aposentado")

        else:
            print("o nadador está aposentado")
    def aquecer(self):
        print("O atleta está está aqucendo para nadar")

    def aposentar(self):
        print("O nadador está preste a se aposentar")

class Ciclista(Atleta):
    def pedalar(self):
        if self.aposentado==False:
            self.aposentado=True
        if self.aposentado==True:
            print("o ciiclista não está aposentado")

        else:
            print("o ciclista está aposentado ")
    def aquecer(self):
        print("O ciclista está aquecendo para pedalar")

    def aposentar(self):
        print("O ciclista faz sua ultima participação de mountain-bike,pois irá se aposentar")
