
import pygame
import sys
import random
import os 

# --- 2. Busca la ruta de la carpeta ---
ruta_base = os.path.abspath(os.path.dirname(__file__))

pygame.init()
pygame.font.init() # Para el texto

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Proyecto 6 - Juego")

# --- Fuente y Puntuación ---
mi_fuente = pygame.font.SysFont("Arial", 30)
puntuacion = 0

# --- Colores ---
COLOR_FONDO = (0, 0, 20) # Azul oscuro
COLOR_MONEDA = (255, 255, 0) # Amarillo
COLOR_METEORO = (255, 0, 0) # Rojo
COLOR_TEXTO = (255, 255, 255) # Blanco

# --- 1. Cargar la imagen de la nave (Sprite) ---
try:
    # Une la ruta de la carpeta con el nombre de la imagen
    ruta_nave = os.path.join(ruta_base, "nave.png")
    nave_img = pygame.transform.scale(pygame.image.load(ruta_nave), (50, 50))
    
    # Creamos el Rect para la nave (su "caja" de colisión)
    # y la ponemos abajo en el centro
    nave_rect = nave_img.get_rect(center=(ANCHO // 2, ALTO - 60))
except:
    print(f"Error: No se encontró 'nave.png' en: {ruta_base}")
    sys.exit()

# --- 2. Objeto para recoger (Puntos) ---
# Usamos un Rect para la colisión
moneda_rect = pygame.Rect(100, 100, 20, 20)

# --- 3. Obstáculo para evitar ---
meteoro_rect = pygame.Rect(200, 50, 40, 40)
velocidad_meteoro = 3

# --- Funciones para reubicar los objetos ---

def nueva_moneda():
    # Pone la moneda en un lugar aleatorio
    moneda_rect.x = random.randint(30, ANCHO - 30)
    moneda_rect.y = random.randint(30, ALTO // 2) # Solo en la mitad de arriba

def nuevo_meteoro():
    # Pone el meteoro arriba en un lugar aleatorio
    meteoro_rect.x = random.randint(30, ANCHO - 30)
    meteoro_rect.y = 0 # Empieza justo arriba de la pantalla

# Ponemos la primera moneda y meteoro en su lugar
nueva_moneda()
nuevo_meteoro()

reloj = pygame.time.Clock()
running = True
while running:
    
    # --- Manejo de eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # --- Mover la nave (con el teclado)  ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave_rect.x -= 7
    if teclas[pygame.K_RIGHT]:
        nave_rect.x += 7
        
    # Límites para que la nave no se salga
    if nave_rect.left < 0:
        nave_rect.left = 0
    if nave_rect.right > ANCHO:
        nave_rect.right = ANCHO
        
    # --- Mover el meteoro ---
    meteoro_rect.y = meteoro_rect.y + velocidad_meteoro
    # Si el meteoro sale por abajo, reaparece arriba
    if meteoro_rect.top > ALTO:
        nuevo_meteoro()

    # --- 4. Colisiones ---
    
    # A. Colisión con Moneda (Recoger objetos) 
    if nave_rect.colliderect(moneda_rect):
        puntuacion = puntuacion + 1
        nueva_moneda() # Mueve la moneda a otro lugar
        
    # B. Colisión con Meteoro (Evitar obstáculos) 
    if nave_rect.colliderect(meteoro_rect):
        print(f"¡Perdiste! Puntuación final: {puntuacion}")
        running = False # Termina el juego
        
    # --- 5. Dibujar ---
    
    # Fondo
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar nave
    pantalla.blit(nave_img, nave_rect)
    # Dibujar moneda (como un círculo)
    pygame.draw.circle(pantalla, COLOR_MONEDA, moneda_rect.center, 10)
    # Dibujar meteoro (como un rectángulo)
    pygame.draw.rect(pantalla, COLOR_METEORO, meteoro_rect)
    
    # Dibujar puntuación en la pantalla 
    texto = mi_fuente.render(f"Puntos: {puntuacion}", True, COLOR_TEXTO)
    pantalla.blit(texto, (10, 10))
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Controlar FPS
    reloj.tick(60)

pygame.quit()
sys.exit()