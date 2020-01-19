# enconding : utf-8

import pygame


class Nave():
    # Guarda as funções relativas a espaçonave e sua posição inicial
    def __init__(self, tela, setting):
        self.tela = tela
        # Carrega a imagem da nave e trata a imagem como retangulos
        self.image = pygame.image.load("Images/ship.bmp") 
        self.rect = self.image.get_rect() # Interpreta a imagem como um retangulo
        self.tela_rect = tela.get_rect() # Divide a tela em retangulos
        #Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.tela_rect.centerx # O centro horizontal da imagem recebe o centro horizontal da tela (Ficando no centro da tela)
        self.rect.bottom = self.tela_rect.bottom # A posição bottom recebe o valor bottom da tela (Ficando em Baixo)
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        self.center = float(self.rect.centerx) # Convertendo de Decimal a Float
        self.setting = setting

    def blitme(self):
        self.tela.blit(self.image, self.rect)

    def update(self):
        # Observa a flag de movimento
        if self.moving_right and self.rect.right < self.tela_rect.right:
            self.center += self.setting.velocidade
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.setting.velocidade

        self.rect.centerx = self.center # Somente a parte inteira será armazenada