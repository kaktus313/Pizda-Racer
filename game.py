import pygame
import sys
import random
# инициализация pygame, создаём экран screen (640x480), делаем заголовок окну, загружаем фон, и рисуем его
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Гонки по пиздорожью")
background = pygame.image.load('background.bmp').convert()
screen.blit(background, (0, 0))

# создаём класс Sprite, он имеет положение x и y, загруженную картинку, и
# chromakey черного фона


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename).convert()
        self.bitmap.set_colorkey((0, 0, 0))
# а также функцию для его отображения
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

racer = Sprite(280, 300, "racer.bmp")
racer.ride = False
enemy = Sprite(0, 0, "enemy.bmp")
roadline = {
    "key": pygame.Surface((10, 30)),
    "posx": 340,
    "posy": 0
}
roadline["key"].fill((255, 255, 255))

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
    if racer.ride is True:
        enemy.x += random.randint(160, 240)
        enemy.y += random.randint(0, 320)
    enemy.render()
    racer.render()
    pygame.display.update()
    pygame.time.delay(400)