from pygame.locals import *
from sys import exit
from tela1 import *
from jogador import *
from tela2 import *
from carro import *
from gameplay import *

pygame.init()
if __name__ == '__main__':
    main()
    screen = pygame.display.set_mode((320,240))
    screen.fill(branco)
    nome_jogador = ask(screen,"Jogador")   
jogador = Jogador(nome_jogador)
escolhaCarro(jogador)
jogo(jogador)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


