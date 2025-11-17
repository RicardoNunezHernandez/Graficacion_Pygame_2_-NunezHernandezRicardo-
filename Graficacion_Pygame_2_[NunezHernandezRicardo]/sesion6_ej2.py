
import pygame
import sys
import random

pygame.init()
pygame.font.init() # Para mostrar texto

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 2 - Recolectar")

# Fuente para el puntaje
mi_fuente = pygame.font.SysFont("Arial", 30)
puntuacion = 0

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 150, 255)
COLOR_MONEDA = (255, 255, 0) # Amarillo

# 1. Jugador
jugador = pygame.Rect(100, 100, 50, 50)

# 2. Moneda (usamos un Rect para colisión fácil)
moneda = pygame.Rect(300, 300, 30, 30)

# Función para mover la moneda
def mover_moneda():
    # Posición aleatoria [cite: 104]
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, ALTO - 50)
    moneda.topleft = (x, y)

reloj = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mover al jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_UP]:
        jugador.y -= 5
    if teclas[pygame.K_DOWN]:
        jugador.y += 5
        
    # 3. Revisamos colisión
    if jugador.colliderect(moneda):
        puntuacion = puntuacion + 1 # Suma puntos 
        mover_moneda() # Mueve la moneda [cite: 105]
        
    # Dibujar
    pantalla.fill(COLOR_FONDO)
    
    # Dibujamos la moneda (como círculo)
    pygame.draw.circle(pantalla, COLOR_MONEDA, moneda.center, 15)
    # Dibujamos al jugador
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador)
    
    # 4. Dibujar puntuación
    texto = mi_fuente.render(f"Puntos: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()