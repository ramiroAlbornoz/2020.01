# Importamos una biblioteca de funciones llamada 'pygame'
import pygame
import random

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

pygame.display.set_caption("Epilepcia Time")
# Iteramos hasta que el usuario haga click sobre el botón de salida.
hecho = False
reloj = pygame.time.Clock()

class Cuadrado():
    def __init__(self, x=0, y=0, movimiento_x=0, movimiento_y=0):
        self.x = random.randrange(0, 300)
        self.y = random.randrange(0, 400)
        self.movimiento_x = random.randrange(1, 5)
        self.movimiento_y = random.randrange(1, 5)

    def change(self, ):
        self.x += self.movimiento_x
        self.y += self.movimiento_y
        if self.x > 360 or self.x < 0:
            self.movimiento_x *= -1
        if self.y > 460 or self.y < 0:
            self.movimiento_y *= -1

        


posicion = Cuadrado()
posicion2 = Cuadrado()
posicion3 = Cuadrado()
posicion4 = Cuadrado()
desp_x = 5
desp_y = 3

# Iteramos en el bucle hasta que hecho == False
while not hecho:

    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            hecho = True  # Marcamos que hemos acabado y abandonamos este bucle

    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.

    # Limpiamos la pantalla y establecemos su fondo.
    pantalla.fill(color_fondo)
    


    pygame.draw.rect(pantalla, color_figura, [posicion.x, posicion.y, 40, 40])
    pygame.draw.rect(pantalla, color_figura, [posicion2.x, posicion2.y, 40, 40])
    pygame.draw.rect(pantalla, color_figura, [posicion3.x, posicion3.y, 40, 40])
    pygame.draw.rect(pantalla, color_figura, [posicion4.x, posicion4.y, 40, 40])

    color_fondo, color_figura = color_figura, color_fondo

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.
    pygame.display.flip()
    posicion.change()
    posicion2.change()
    posicion3.change()
    posicion4.change()

    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    # Lo dejamos aquí y usamos toda la CPU que podamos.
    reloj.tick(30)

# Pórtate bien con el IDLE
pygame.quit()