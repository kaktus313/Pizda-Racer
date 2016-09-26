import pygame
import random
import zhostkii_racer
import sys

screen = zhostkii_racer.get_screen(640,480)
pygame.init()

pygame.display.set_caption("Гонки по бездорожью")
background = pygame.image.load('background.bmp').convert()

# определяем гонщика
racer = zhostkii_racer.Sprite(280, 300, "racer.bmp")
# нам нужна переменная, чтобы понимать, едем ли мы вообще или нет
startgame = False
# это враг (-100 потому что он пока за экраном)
enemy = zhostkii_racer.Sprite(280, -100, "enemy.bmp")
# дорожная линия, создающая иллюзию движения, она будет 10x30 по середине вверху экрана
roadline = {
    "key": pygame.Surface((10, 30)),
    "posx": 340,
    "posy": 0
}
# заполняем линию белым цветом
roadline["key"].fill((255, 255, 255))
# это нужно чтобы не нажимать каждый раз кнопку для движения
pygame.key.set_repeat(1, 1)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
intromusic = pygame.mixer.Sound("coolorshit.ogg")
intromusic.play(0)
backmusic = pygame.mixer.Sound("backmusic.ogg")
gameovermusic = pygame.mixer.Sound("gameover.ogg")


def gameover():
    global startgame
    startgame = False
    racer.x = -150
    racer.y = -150
    enemy.x = -300
    enemy.y = -300
    pygame.mixer.stop()
    gameovermusic.play(0)


# идёт игра
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                startgame = True
            if startgame:
                if event.key == pygame.K_LEFT and racer.x > 120:
                    racer.x -= 10
                if event.key == pygame.K_RIGHT and racer.x < 440:
                    racer.x += 10

    if zhostkii_racer.intersect(racer.x, enemy.x, racer.y, enemy.y, 30, 40):
        gameover()

    screen.blit(background, (0, 0))
    for i in range(15):
        if startgame:
            screen.blit(roadline["key"], (roadline["posx"], roadline["posy"]))
            roadline["posy"] += i
    if startgame:
        intromusic.stop()
        backmusic.set_volume(0.5)
        backmusic.play(-1)
        enemy.x += random.randint(-20, 20)
        if enemy.x <= 120:
            enemy.x += 20
        elif enemy.x >= 440:
            enemy.x -= 20
        enemy.y += 1

    enemy.render(screen)
    racer.render(screen)
    pygame.display.update()