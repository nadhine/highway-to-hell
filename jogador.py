from carro import *

class Jogador():
    def __init__(self,nome):
        self.nome = nome
        self.carro = Carro()
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        if len(nome) > 1 and len(nome) <= 10:
            self.nome = nome
        else:
            return
    def getCarro(self):
        return self.carro
    def setCarro(self,carro):
        self.carro = carro
