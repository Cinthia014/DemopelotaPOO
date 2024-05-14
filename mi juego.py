import pygame # librería para trabajar con videojuegos
from pelota import Pelota
from pygame.locals import *

pygame.init() # inicializar juego
screen = pygame.display.set_mode((800, 600)) # tamaño (ancho, alto)

p = Pelota()

clock = pygame.time.Clock() # <--- crear un reloj
 game_over = False
while not  game_over:
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    clock.tick(50) # <--- limitar que el juego se ejecute 50 veces por segundo
    screen.fill((0, 0, 0)) # <--- fondo
    screen.blit(p.ball, p.ball_rect) # dibujar la pelota
    p.moverse(800,600)
    pygame.display.update()  # actualizar pantalla
pygame.quit()
