import pygame

pygame.init()

hecho = False
rayo = False
reloj = pygame.time.Clock()

dimensiones = (626, 417)

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Programacion 2")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

fondo = pygame.image.load('fondo.jpg').convert()
nave = pygame.image.load('nave.png').convert()
nave.set_colorkey(NEGRO)
nave45 = pygame.image.load('nave45.png').convert()
nave45.set_colorkey(NEGRO)
nave90 = pygame.image.load('nave90.png').convert()
nave90.set_colorkey(NEGRO)
nave135 = pygame.image.load('nave135.png').convert()
nave135.set_colorkey(NEGRO)
nave180 = pygame.image.load('nave180.png').convert()
nave180.set_colorkey(NEGRO)
nave225 = pygame.image.load('nave225.png').convert()
nave225.set_colorkey(NEGRO)
nave270 = pygame.image.load('nave270.png').convert()
nave270.set_colorkey(NEGRO)
nave315 = pygame.image.load('nave315.png').convert()
nave315.set_colorkey(NEGRO)

personaje = nave

pos = [300, 200]
pos_anterior = pos
salto_x = 0
salto_y = 0

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:  
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                salto_y = -2
                personaje = nave
            if evento.key == pygame.K_DOWN:
                salto_y = 2
                personaje = nave180
            if evento.key == pygame.K_LEFT:
                salto_x = -2
                personaje = nave270
            if evento.key == pygame.K_RIGHT:
                salto_x = 2
                personaje = nave90
            if evento.key == pygame.K_SPACE:
                rayo = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP:
                tecla_anterior = 0
                salto_y = 0
            if evento.key == pygame.K_DOWN:
                salto_y = 0
            if evento.key == pygame.K_LEFT:
                salto_x = 0
            if evento.key == pygame.K_RIGHT:
                salto_x = 0
            if evento.key == pygame.K_SPACE:
                rayo = False

    pantalla.fill(NEGRO)
    pantalla.blit(fondo, (0, 0))

    if rayo:
        if personaje == nave:
            pygame.draw.line(pantalla, BLANCO, [pos[0], pos[1] - 20], [pos[0], 0], 2)
        if personaje == nave180:
            pygame.draw.line(pantalla, ROJO, [pos[0], pos[1] - 20], [pos[0], 500], 2)
        if personaje == nave90:
            pygame.draw.line(pantalla, AZUL, [pos[0], pos[1] - 17], [700, pos[1] - 17], 2)
        if personaje == nave270:
            pygame.draw.line(pantalla, VERDE, [pos[0], pos[1] - 17], [0, pos[1] - 17], 2)

    pygame.mouse.set_visible(False)
    offset = (pos[0] - 25, pos[1] - 40)
    pos[0] += salto_x
    pos[1] += salto_y

    if pos[0] > pos_anterior[0]:
        personaje = nave90
    if pos[0] < pos_anterior[0]:
        personaje = nave270
    if pos[1] < pos_anterior[1]:
        personaje = nave
    if pos[1] > pos_anterior[1]:
        personaje = nave180
    
    pantalla.blit(personaje, offset)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
