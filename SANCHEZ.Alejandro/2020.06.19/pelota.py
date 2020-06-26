import pygame
class Pelota():
    def __init__(self, x=0, y=0, desp_x=1, desp_y=1, radio=20, color=None):
        self.x = x
        self.y = y
        self.desp_x = desp_x
        self.desp_y = desp_y
        self.color = color
        self.radio = radio
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
    @property
    def desp_x(self):
        return self.__desp_x
    @desp_x.setter
    def desp_x(self, value):
        self.__desp_x = value
    @property
    def desp_y(self):
        return self.__desp_y
    @desp_y.setter
    def desp_y(self, value):
        self.__desp_y = value
    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, value):
        self.__radio = value
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value
    def draw(self, display):
        pygame.draw.circle(display, self.color, [self.x, self.y], self.radio)
    def move(self, ancho, alto):
        self.x += self.desp_x
        self.y += self.desp_y
        if self.x < 20 or self.x > ancho - 20:
            self.desp_x *= -1
        if self.y < 20 or self.y > alto - 20:
            self.desp_y *= -1