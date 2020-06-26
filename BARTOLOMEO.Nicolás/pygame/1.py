# Importamos una biblioteca de funciones llamada 'pygame'
import pygame

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

coord_x = 5
coord_y = 5


coord_x2 = 60
coord_y2 = 60

desp_x = 5
desp_y = 3

desp_x2 = 7
desp_y2 = 4

# Iteramos en el bucle hasta que hecho == False
while not hecho:

    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            hecho = True  # Marcamos que hemos acabado y abandonamos este bucle

    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.

    # Limpiamos la pantalla y establecemos su fondo.
    pantalla.fill(color_fondo)

    pygame.draw.rect(pantalla, color_figura, [coord_x, coord_y, 40, 40])
    pygame.draw.rect(pantalla, color_figura, [coord_x2, coord_y2, 40, 40])
    # color_fondo, color_figura = color_figura, color_fondo

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.
    pygame.display.flip()

    coord_x += desp_x
    coord_y += desp_y

    coord_x2 += desp_x2
    coord_y2 += desp_y2

    if coord_x > 360 or coord_x < 0:
        desp_x *= -1
    if coord_y > 460 or coord_y < 0:
        desp_y *= -1
    if coord_x2 > 360 or coord_x2 < 0:
        desp_x2 *= -1
    if coord_y2 > 460 or coord_y2 < 0:
        desp_y2 *= -1
    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    # Lo dejamos aquí y usamos toda la CPU que podamos.
    reloj.tick(30)

# Pórtate bien con el IDLE
pygame.quit()