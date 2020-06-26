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

nave = pygame.image.load('nave.png').convert()
fondo = pygame.image.load('fondo.jpg').convert()
nave.set_colorkey(NEGRO)

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:  
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            rayo = True
        if evento.type == pygame.MOUSEBUTTONUP:
            rayo = False
    
    pantalla.fill(NEGRO)
    pantalla.blit(fondo, (0, 0))

    if rayo:
        pygame.draw.line(pantalla, BLANCO, [pos[0], pos[1] - 20], [pos[0], 0], 2)

    pos = pygame.mouse.get_pos()
    offset = (pos[0] - 25, pos[1] - 40)

    pantalla.blit(nave, offset)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
