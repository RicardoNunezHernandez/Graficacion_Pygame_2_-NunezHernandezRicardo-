
import pygame
import sys
import os 

# --- 2. Esta es la parte nueva ---
# Busca la ruta de la carpeta DONDE ESTÁ ESTE SCRIPT
ruta_base = os.path.abspath(os.path.dirname(__file__))
# --------------------------------

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1 - Escalar Imagen")

# 3. Carga la imagen ORIGINAL
try:
    # --- 4. Une la ruta de la carpeta con el nombre del archivo ---
    ruta_imagen = os.path.join(ruta_base, "auto.png")
    
    imagen_original = pygame.image.load(ruta_imagen)
except:
    print(f"Error: No se encontró la imagen en la ruta: {ruta_imagen}")
    sys.exit()

# Guardamos el tamaño original
ancho_original, alto_original = imagen_original.get_size()

# 2. Variable de escala
escala = 1.0

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                escala = escala + 0.1
            if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                escala = escala - 0.1
                if escala < 0.1:
                    escala = 0.1

    nuevo_ancho = int(ancho_original * escala)
    nuevo_alto = int(alto_original * escala)
    
    imagen_escalada = pygame.transform.scale(imagen_original, (nuevo_ancho, nuevo_alto))

    pantalla.fill((30, 30, 30))
    pos_x = (ANCHO - nuevo_ancho) // 2
    pos_y = (ALTO - nuevo_alto) // 2
    pantalla.blit(imagen_escalada, (pos_x, pos_y))
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()