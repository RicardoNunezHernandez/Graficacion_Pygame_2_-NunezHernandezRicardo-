

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1 - Rebote Acelerado")

COLOR_FONDO = (0, 0, 0)
COLOR_BOLA = (255, 255, 255)

# Posición inicial de la bola
x = ANCHO // 2
y = ALTO // 2
radio = 20

# Velocidad inicial
velocidad_x = 3
velocidad_y = 3

# 1. Reloj para controlar los FPS
reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mover la bola
    x = x + velocidad_x
    y = y + velocidad_y
    
    # Rebotar en bordes (arriba/abajo)
    if y + radio > ALTO or y - radio < 0:
        velocidad_y = -velocidad_y
        
    # Rebotar en bordes (izquierda/derecha)
    if x + radio > ANCHO or x - radio < 0:
        velocidad_x = -velocidad_x
        
        # 2. Incrementar velocidad en 0.1 cada vez que rebota
        if velocidad_x > 0:
            velocidad_x = velocidad_x + 0.1
        else:
            velocidad_x = velocidad_x - 0.1
            
        print(f"Nueva velocidad X: {velocidad_x}")

    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.circle(pantalla, COLOR_BOLA, (x, y), radio)
    
    # 3. Asegurar 60 FPS
    reloj.tick(60)
    
    pygame.display.flip()

pygame.quit()
sys.exit()