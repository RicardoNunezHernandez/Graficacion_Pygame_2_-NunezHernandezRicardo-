

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 3 - Gravedad")

COLOR_FONDO = (20, 20, 20)
COLOR_BOLA = (255, 165, 0) # Naranja

# Posición inicial
x = ANCHO // 2
y = 100
radio = 20

# 1. Velocidad vertical (empieza en 0)
velocidad_y = 0
gravedad = 0.5 # [cite: 75]

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 2. Aplicamos la gravedad a la velocidad
    velocidad_y = velocidad_y + gravedad
    
    # 3. Movemos la pelota
    y = y + velocidad_y
    
    # 4. Rebotar en el suelo
    if y + radio > ALTO:
        y = ALTO - radio # Pone la pelota justo en el suelo
        velocidad_y = -velocidad_y # Invierte la dirección
        
        # 5. Pierde 20% de energía (se queda con 80%)
        velocidad_y = velocidad_y * 0.80 
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.circle(pantalla, COLOR_BOLA, (x, y), radio)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()