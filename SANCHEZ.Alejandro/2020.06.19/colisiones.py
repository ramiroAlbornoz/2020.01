# Importamos una biblioteca de funciones llamada 'pygame'
import pygame
import random
import math
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
coord_x_1 = random.randrange(0, 400)
coord_y_1 = 20
coord_x_2 = 20
coord_y_2 = random.randrange(0, 500)
desp_x_1 = 5
desp_y_1 = 3
desp_x_2 = 8
desp_y_2 = 5
# Iteramos en el bucle hasta que hecho == False
while not hecho:
    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            hecho = True  # Marcamos que hemos acabado y abandonamos este bucle
    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.
    # Limpiamos la pantalla y establecemos su fondo.
    pantalla.fill(color_fondo)
    pygame.draw.circle(pantalla, color_figura, [coord_x_1, coord_y_1], 20)
    pygame.draw.circle(pantalla, ROJO, [coord_x_2, coord_y_2], 20)
    # color_fondo, color_figura = color_figura, color_fondo
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.
    pygame.display.flip()
    distancia = math.sqrt(pow(coord_x_1 - coord_x_2, 2) + pow(coord_y_1 - coord_y_2, 2))
    coord_x_1 += desp_x_1
    coord_y_1 += desp_y_1
    coord_x_2 += desp_x_2
    coord_y_2 += desp_y_2
    if coord_x_1 > 380 or coord_x_1 < 20 or distancia < 50:
        desp_x_1 *= -1
    if coord_y_1 > 480 or coord_y_1 < 20:
        desp_y_1 *= -1
    if coord_x_2 > 380 or coord_x_2 < 20 or distancia < 50:
        desp_x_2 *= -1
    if coord_y_2 > 480 or coord_y_2 < 20:
        desp_y_2 *= -1
    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    # Lo dejamos aquí y usamos toda la CPU que podamos.
    reloj.tick(40)
# Pórtate bien con el IDLE
pygame.quit()