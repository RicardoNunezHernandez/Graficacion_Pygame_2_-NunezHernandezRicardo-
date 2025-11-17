
import pygame
import sys
import os 

# --- 2. Busca la ruta de la carpeta donde está este script ---
ruta_base = os.path.abspath(os.path.dirname(__file__))

pygame.init()

pantalla = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Ejercicio 2 - Sprite Animado")

# 3. Cargamos los 4 frames en una lista
frames = []
nombres_frames = ["frame1.png", "frame2.png", "frame3.png", "frame4.png"]

try:
    for nombre in nombres_frames:
        # --- 4. Une la ruta de la carpeta con el nombre de cada frame ---
        ruta_completa = os.path.join(ruta_base, nombre)
        frames.append(pygame.image.load(ruta_completa))
except:
    print(f"Error: No se encontraron los archivos de frames en: {ruta_base}")
    sys.exit()

# Para controlar qué frame mostrar
indice_frame_actual = 0
# Para controlar el tiempo
ultimo_cambio = pygame.time.get_ticks()
tiempo_por_frame = 100 # 100 milisegundos

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Control de la animación
    ahora = pygame.time.get_ticks() 
    
    if ahora - ultimo_cambio > tiempo_por_frame:
        ultimo_cambio = ahora 
        indice_frame_actual = indice_frame_actual + 1
        
        if indice_frame_actual >= 4:
            indice_frame_actual = 0

    imagen_actual = frames[indice_frame_actual]

    # Dibujar
    pantalla.fill((50, 50, 50))
    pantalla.blit(imagen_actual, (150, 150))
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()