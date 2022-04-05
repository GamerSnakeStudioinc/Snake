import pygame
import random
from array import *

pygame.init()

class snake(object):
    def head_move_and_draw():
        global xt, yt
        xt = x[0]
        yt = y[0]
        x[0] += moveX
        y[0] += moveY
        x[0] = Border_Check_X(x[0])
        y[0] = Border_Check_Y(y[0])
        pygame.draw.rect(srf, clg, (x[0], y[0], 10, 10))


    def tail_build_and_draw():
        if len(x) > 2:
            for n in range(1, len(x) - 1):
                x[len(x) - n] = x[len(x) - n - 1]
                y[len(x) - n] = y[len(x) - n - 1]
                pygame.draw.rect(srf, clg, (x[len(x) - n], y[len(x) - n], 10, 10))
        if len(x) > 1:
            x[1] = xt
            y[1] = yt
            pygame.draw.rect(srf, clg, (x[1], y[1], 10, 10))

        pass


    def direction():
        global moveY, moveX
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT] and backwordsch(moveX, speed):
            moveX = -speed
            moveY = 0
        if press[pygame.K_RIGHT] and backwordsch(moveX, -speed):
            moveX = speed
            moveY = 0
        if press[pygame.K_UP] and backwordsch(moveY, speed):
            moveY = -speed
            moveX = 0
        if press[pygame.K_DOWN] and backwordsch(moveY, -speed):
            moveY = speed
            moveX = 0
        pass


class food():
    def draw():
        pygame.draw.rect(srf, clr, (xF, yF, 10, 10))
        pass


    def eaten_check():
        global xF, yF, x, y
        if x[0] == xF and y[0] == yF or press[pygame.K_e]:
            x.append(0)
            y.append(0)
            xF = int(round(random.randint(1, W) / 100, 1) * 100) - 10
            yF = int(round(random.randint(1, H) / 100, 1) * 100) - 10
            pass




def backwordsch(a,b):
    return a != b
    pass


def Border_Check_X(a):
    if a >= BorderRIGHT:
        a = BorderLEFT
        return a

    if a < BorderLEFT:
        a = BorderRIGHT - 10
    return a
    pass


def Border_Check_Y(a):
    if a >= BorderDOWN:
        a = BorderUP
        return a

    if a < BorderUP:
        a = BorderDOWN - 10
    return a
    pass


def field_build():
    global snake_on_field
    for n in range(0, int(W / 10)):
        for m in range(0, int(W / 10)):
            if m == int(xF / 10) and n == int(yF / 10):
                field[n][m] = 2
            for i in range(0, len(x)):
                if m == int(x[i] / 10) and n == int(y[i] / 10):
                    if field[n][m] != 1:
                        field[n][m] = 1
                        snake_on_field += 1

FPS = 15
clock = pygame.time.Clock()
W, H = 600, 600
x = array('i', [W // 2])
y = array('i', [H // 2])
xD = array('i', [W // 2])
yD = array('i', [H // 2])

# colors
clg = (0, 255, 0)
clbl = (0, 0, 0)
clr = (255, 0, 0)
# ______________________

srf = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")


BorderUP = BorderLEFT = 0
BorderDOWN = H
BorderRIGHT = W
speed = 10

moveX = 0
moveY = speed

xF = int(round(random.randint(1, W) / 100, 1) * 100)
yF = int(round(random.randint(1, H) / 100, 1) * 100)

xt = 0
yt = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    press = pygame.key.get_pressed()

    field = [[0] * int((W / 10)) for i in range(int((H / 10)))]
    snake_on_field = 0


    food.eaten_check()


    srf.fill(clbl)
    snake.direction()
    snake.head_move_and_draw()

    snake.tail_build_and_draw()

    field_build()
    if snake_on_field < len(x):
        exec("LOOOSE(")

    food.draw()
    pygame.display.update()
    clock.tick(FPS)