from pygame.locals import *
from sys import exit
from tela1 import *
from jogador import *
from tela2 import *
from carro import *
from gameplay import *

pygame.init()
main()
screen = pygame.display.set_mode((320,240))
screen.fill((255,255,255))
nome_jogador = ask(screen,"Jogador")   
jogador = Jogador(nome_jogador)
escolhaCarro(jogador)
jogo(jogador)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

