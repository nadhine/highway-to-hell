import pygame
from pygame.locals import *
from sys import exit



def jogo(jogador):
    tela = pygame.display.set_mode((320, 240), 0, 32)
    x = 160
    y = 175

    direcmov = 0
    movcima = 0

    sprite = jogador.getCarro().getImagem()

    pygame.mixer.music.load("ACDC - Highway to hell.mp3")
    pygame.mixer.music.play()
    pygame.key.set_repeat(500, 50)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN :
                if event.key == K_d :
                    direcmov = +10
                elif event.key == K_a:
                    direcmov = -10
                elif event.key == K_w:
                    pass
            elif event.type == KEYUP:
                direcmov = 0
                movcima = 0
            x += direcmov
            #y += movcima
            #movcima = 0

        tela.blit(pygame.image.load("pista.png").convert(), (0, 0))
        tela.blit(pygame.image.load(sprite).convert(), (x,y))

        pygame.display.update()
