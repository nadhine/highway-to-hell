import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from sys import exit
from jogador import *

branco = (255, 255, 255)


def escolhaCarro(jogador): 
    tela = pygame.display.set_mode((320,240))
    posicionando = ""
    posicao = ""
    carro = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEMOTION:
                posicionando = (pygame.mouse.get_pos())
            elif event.type == MOUSEBUTTONDOWN:
                posicao = posicionando
                print (posicao[0])
                if int(posicao[1]) >= 130 and int(posicao[1])<= 195:
                    if int(posicao[0]) >= 0 and int(posicao[0]) <= 61:
                        jogador.getCarro().setImagem("car1.png")
                        return 
                    elif int(posicao[0]) >= 65 and int(posicao[0])<= 125:
                        jogador.getCarro().setImagem("car2.png")
                        return
                    elif int(posicao[0]) >= 130 and int(posicao[0]) <= 190:
                        jogador.getCarro().setImagem("car3.png")
                        return
                    elif int(posicao[0]) >= 195 and int(posicao[0]) <= 250:
                        jogador.getCarro().setImagem("car4.png")
                        return
                    elif int(posicao[0]) >= 255 and int(posicao[0]) <= 315:
                        jogador.getCarro().setImagem("car5.png")
                        return
        tela.fill(branco)
        tela.blit(pygame.image.load("car1.png").convert(), (0,130))
        tela.blit(pygame.image.load("car2.png").convert(), (65,130))
        tela.blit(pygame.image.load("car3.png").convert(), (130,130))
        tela.blit(pygame.image.load("car4.png").convert(), (195,130))
        tela.blit(pygame.image.load("car5.png").convert(), (255,130))
        tela.blit(pygame.font.SysFont("arial", 18).render("Escolha seu Carro: ", True, (0,0,0)), (60,30))
        pygame.display.update()
    
