

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 3 - Evitar")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 150, 255) # Azul
COLOR_ENEMIGO = (255, 0, 0) # Rojo

# 1. Jugador
jugador = pygame.Rect(100, 500, 40, 40)

# 2. Enemigo
enemigo = pygame.Rect(100, 200, 50, 50)
velocidad_enemigo = 5

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mover al jugador (solo de lado a lado)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
        
    # 3. Mover al enemigo
    enemigo.x = enemigo.x + velocidad_enemigo
    
    # Rebotar enemigo en las paredes
    if enemigo.right > ANCHO or enemigo.left < 0:
        velocidad_enemigo = -velocidad_enemigo
        
    # 4. Revisamos colisión (Game Over)
    if jugador.colliderect(enemigo):
        print("¡Perdiste!")
        running = False # Termina el juego 
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador)
    pygame.draw.rect(pantalla, COLOR_ENEMIGO, enemigo)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()# Guarda esto como sesion6_ej3.py

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 3 - Evitar")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 150, 255) # Azul
COLOR_ENEMIGO = (255, 0, 0) # Rojo

# 1. Jugador
jugador = pygame.Rect(100, 500, 40, 40)

# 2. Enemigo
enemigo = pygame.Rect(100, 200, 50, 50)
velocidad_enemigo = 5

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mover al jugador (solo de lado a lado)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
        
    # 3. Mover al enemigo
    enemigo.x = enemigo.x + velocidad_enemigo
    
    # Rebotar enemigo en las paredes
    if enemigo.right > ANCHO or enemigo.left < 0:
        velocidad_enemigo = -velocidad_enemigo
        
    # 4. Revisamos colisión (Game Over)
    if jugador.colliderect(enemigo):
        print("¡Perdiste!")
        running = False # Termina el juego 
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador)
    pygame.draw.rect(pantalla, COLOR_ENEMIGO, enemigo)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()