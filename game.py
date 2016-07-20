import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Гонки по пиздорожью")
background = pygame.image.load('background.bmp').convert()
screen.blit(background, (0, 0))


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename).convert()
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

racer = Sprite(280, 300, "racer.bmp")
racer.ride = False
roadline = {
    "key": pygame.Surface((10, 30)),
    "posx": 340,
    "posy": 0
}
roadline["key"].fill((255, 255, 255))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                racer.x -= 10
            if event.key == pygame.K_RIGHT:
                racer.x += 10
            if event.key == pygame.K_UP:
                racer.ride = True

    screen.blit(background, (0, 0))
    for i in range(2000):
        if racer.ride is True:
            screen.blit(roadline["key"], (roadline["posx"], roadline["posy"]))
            roadline["posy"] += i
    racer.render()
    pygame.display.update()