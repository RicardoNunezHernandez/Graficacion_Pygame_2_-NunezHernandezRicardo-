

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1 - Colisión y Color")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 0, 255) # Azul
COLOR_OBJETIVO = (255, 0, 0) # Rojo
COLOR_COLISION = (0, 255, 0) # Verde [cite: 99]

# 1. Creamos los rectángulos
# (x, y, ancho, alto)
jugador = pygame.Rect(100, 100, 50, 50)
objetivo = pygame.Rect(400, 300, 100, 100)

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mover al jugador con las flechas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_UP]:
        jugador.y -= 5
    if teclas[pygame.K_DOWN]:
        jugador.y += 5
        
    # 2. Revisamos si hay colisión
    if jugador.colliderect(objetivo):
        color_actual_jugador = COLOR_COLISION
    else:
        color_actual_jugador = COLOR_JUGADOR
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, color_actual_jugador, jugador)
    pygame.draw.rect(pantalla, COLOR_OBJETIVO, objetivo)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()