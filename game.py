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
startgame = False
enemy = Sprite(280, -100, "enemy.bmp")
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
            if event.key == pygame.K_LEFT and racer.x != 120:
                racer.x -= 10
            if event.key == pygame.K_RIGHT and racer.x != 440:
                racer.x += 10
            if event.key == pygame.K_UP:
                startgame = True

    screen.blit(background, (0, 0))
    for i in range(2000):
        if startgame is True:
            screen.blit(roadline["key"], (roadline["posx"], roadline["posy"]))
            roadline["posy"] += i
    if startgame is True:
        enemy.x += random.randint(-20, 20)
        enemy.y += 10
    enemy.render()
    racer.render()
    pygame.display.update()
    pygame.time.delay(30)