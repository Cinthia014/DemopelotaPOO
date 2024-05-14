import pygame

class Pelota:
    def __init__(self):
        self.ball = pygame.image.load('imagenes/football.png')
        self.ball = self.ball.convert_alpha()
        self.ball_rect = self.ball.get_rect()
        self.posicionX = 200
        self.posicionY = 200
        self.velocidadX = 3.0
        self.velocidadY = 3.0

    def moverse(self, ancho, alto):
        if self.posicionX <= 0 or self.posicionX + \
                self.ball.get_width() >= ancho:
            self.velocidadX *= -1
        if self.posicionY <= 0 or self.posicionY + \
                self.ball.get_height() >= alto:
            self.velocidadY *= -1
        self.posicionX += self.velocidadX
        self.posicionY += self.velocidadY
        self.ball_rect[0] = self.posicionX
        self.ball_rect[1] = self.posicionY
