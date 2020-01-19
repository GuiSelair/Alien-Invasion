# encoding: utf-8

import sys
import pygame
from settings import Settings
from nave import Nave
import game_functions as game_functions

# ------------ Alien Invasion -------------
# ---- Janela de execução -----------

def run_game():
    # Inicializa o jogo e define resolução
    pygame.init()
    config = Settings()
    tela = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("Alien Invasion")
    nave = Nave(tela, config)

    while True:
        # Laço principal do jogo
        game_functions.check_events(nave)
        nave.update()
        game_functions.update_screen(config, tela, nave)


run_game()