import pygame
from pygame.locals import *
from sys import exit
from carro import *


def jogo(jogador):
    tela = pygame.display.set_mode((320, 240), 0, 32)
    xCarro = 160
    yCarro = 175
    xPista = 0
    yPista = -2320

    velocidade = 0
    sprite = jogador.getCarro().getImagem()
    carro = jogador.getCarro()
    carro.setMovimento(10)
    mov = carro.getMovimento()
    carro.setVelocidade(5)
    vel= carro.getVelocidade()

    pygame.mixer.music.load("ACDC - Highway to hell.mp3")
    pygame.mixer.music.play()
    pygame.key.set_repeat(50, 5)
    while True:
        for event in pygame.event.get():
            direcmov = 0
            if event.type == QUIT:
                exit()                
            elif event.type == KEYDOWN :
                if event.key == K_d and xCarro < 220:
                    direcmov = mov
                elif event.key == K_a and xCarro > 40 :
                    direcmov = -mov
                elif event.key == K_w:
                    velocidade += vel
            xCarro += direcmov
        if yPista < -2080:
            yPista += velocidade

        tela.blit(pygame.image.load("pistascroll.png").convert(), (xPista,yPista))
        tela.blit(pygame.image.load(sprite).convert(), (xCarro,yCarro))
        tela.blit(pygame.font.SysFont("arial", 14).render("Jogador: "+jogador.getNome(), True, (220,220,220)), (60,30))

        pygame.display.update()
