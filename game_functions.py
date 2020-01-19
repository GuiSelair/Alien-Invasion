# encoding: utf-8

import sys
import pygame

def check_events(nave):
    # Observa e responde ao pressionamente de teclas e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Fecha o game
            sys.exit()
        elif event.type == pygame.KEYDOWN:  
            check_keydown_events(event, nave)
        elif event.type == pygame.KEYUP:    
            check_keyup_events(event, nave)

def update_screen(config, tela, nave):
    # Atualiza as imagens na tela
    tela.fill(config.bg_color)
    nave.blitme()
    pygame.display.flip()      # Mantem a tela atualizada a cada volta do laço

def check_keydown_events(event, nave):  # Observa o evento de KEYDOWN
    if event.key == pygame.K_RIGHT:
        # Move a nave para a direita
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move a nave para a esquerda
        nave.moving_left = True

def check_keyup_events(event, nave):    # Observa o evento de KEYUP
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False