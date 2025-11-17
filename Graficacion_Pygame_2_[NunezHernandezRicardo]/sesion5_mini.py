
import pygame
import sys
import math
import os 

# --- 2. Busca la ruta de la carpeta ---
ruta_base = os.path.abspath(os.path.dirname(__file__))

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Proyecto 5 - Nave al Ratón")

# 3. Cargar la imagen original
try:
    # --- 4. Une la ruta con el nombre del archivo ---
    ruta_nave = os.path.join(ruta_base, "nave.png")
    
    imagen_original = pygame.transform.scale(pygame.image.load(ruta_nave), (50, 50))
except:
    print(f"Error: No se encontró 'nave.png' en: {ruta_base}")
    sys.exit()

# Posición de la nave
x = ANCHO // 2
y = ALTO // 2
velocidad = 5
angulo = 0

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # --- Rotación ---
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    dx = mouse_x - x
    dy = mouse_y - y
    
    angulo_rad = math.atan2(-dy, dx)
    angulo = math.degrees(angulo_rad)
    
    # --- Movimiento ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        x = x + math.cos(angulo_rad) * velocidad
        y = y - math.sin(angulo_rad) * velocidad
    
    # --- Dibujar ---
    pantalla.fill((0, 0, 0))
    
    imagen_rotada = pygame.transform.rotate(imagen_original, angulo)
    rect_rotado = imagen_rotada.get_rect(center = (x, y))
    
    pantalla.blit(imagen_rotada, rect_rotado)
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()