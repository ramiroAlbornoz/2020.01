# Importamos una biblioteca de funciones llamada 'pygame'
import pygame
import random
import math
from pelota import Pelota
# Inicializamos el motor de juegos
pygame.init()
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
color_fondo = NEGRO
color_figura = BLANCO
# Establecemos el largo y alto de la pantalla
dimensiones = (400, 500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Divertido Juego del Profesor Craven")
# Iteramos hasta que el usuario haga click sobre el botón de salida.
hecho = False
reloj = pygame.time.Clock()
pelota1 = Pelota(random.randrange(0, 400), 20, 5, 3, 20, BLANCO)
pelota2 = Pelota(20, random.randrange(0, 500), 8, 5, 20, ROJO)
pelota3 = Pelota(random.randrange(0, 400), random.randrange(0, 500), 2, 2, 20, AZUL)
# Iteramos en el bucle hasta que hecho == False
while not hecho:
    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            hecho = True  # Marcamos que hemos acabado y abandonamos este bucle
    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.
    # Limpiamos la pantalla y establecemos su fondo.
    pantalla.fill(color_fondo)
    pelota1.draw(pantalla)
    pelota2.draw(pantalla)
    pelota3.draw(pantalla)
    pelota1.move(400, 500)
    pelota2.move(200, 250)
    pelota3.move(300, 400)
    # color_fondo, color_figura = color_figura, color_fondo
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.
    pygame.display.flip()
    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    # Lo dejamos aquí y usamos toda la CPU que podamos.
    reloj.tick(40)
# Pórtate bien con el IDLE
pygame.quit()