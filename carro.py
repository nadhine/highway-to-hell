class Carro():
    def __init__(self,imagem = "",posicao=(0,0),movimento=0,velocidade=0):
        self._imagem = imagem
        self._posicao = posicao
        self._movimento = movimento
        self._velocidade = velocidade

    def getImagem (self):
        return str(self._imagem)
    
    def setImagem(self, imagem):
        self._imagem = imagem
        
    def getPosicao (self):
        return self.posicao
    
    def setPosicao (self,posicao):
        self._posicao = posicao
        
    def getMovimento (self):
        return self._movimento
    
    def setMovimento (self, movimento):
        self._movimento = movimento
        
    def getVelocidade (self):
        return self._velocidade
    
    def setVelocidade (self,velocidade):
        self._velocidade = velocidade

    def movDireita(self):
        pass
        # os mov direita e esquerda recebem o retorno da entrada do jogador na classe jogo, muda a posicao e retorna pro jogo a posicao modificada
    def modEsquerda():
        pass
    def acelera():
        #acelera e freia vaum ser iguais aos movs, mas no eixo y ... n mexer neles ateh terminar o eixo x 
        pass
    def freia():
        pass
        
