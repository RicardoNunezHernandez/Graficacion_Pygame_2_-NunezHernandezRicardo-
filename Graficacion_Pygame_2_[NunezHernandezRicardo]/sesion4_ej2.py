

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 2 - Pulsación")

COLOR_FONDO = (0, 0, 0)
COLOR_BOLA = (0, 255, 255) # Cyan

# 1. Radio inicial y dirección
radio = 20
direccion_crecimiento = 1 # 1 = creciendo, -1 = encogiendo

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 2. Cambiamos el radio
    radio = radio + direccion_crecimiento
    
    # 3. Cambiamos la dirección si llega a los límites (20 y 50)
    if radio >= 50: # 
        direccion_crecimiento = -1 # Encoger
    
    if radio <= 20: # 
        direccion_crecimiento = 1 # Crecer
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    pygame.draw.circle(pantalla, COLOR_BOLA, (ANCHO // 2, ALTO // 2), radio)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()