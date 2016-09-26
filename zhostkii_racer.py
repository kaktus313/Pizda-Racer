import pygame




class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename).convert()
        self.bitmap.set_colorkey((0, 0, 0))
# а также функцию для его отображения

    def render(self,screen):
        screen.blit(self.bitmap, (self.x, self.y))
# функция называется "пересечение", возвращает True координаты объектов (и их смещения в зависимости от
# размеров) пересекаются


def intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2):
        return 1
    else:
        return 0

def get_screen(x,y):
    return pygame.display.set_mode((x, y))