import pygame
import random
from array import *

pygame.init()

class snake(object):
    def move_head():
        global xt, yt
        xt = x[0]
        yt = y[0]
        x[0] += moveX
        y[0] += moveY
        x[0] = Border_Check_X(x[0])
        y[0] = Border_Check_Y(y[0])
    def draw():
        pygame.draw.rect(srf, clg, (x[0], y[0], 10, 10))
        pass


    def tail_build_and_draw():
        global lenght
        lenght -= 1
        if snake.count(lenght) == 3:
            x[1] = xt
            y[1] = yt
        elif snake.count(lenght) > 2:
            for i in range(0, lenght):
                x[lenght - i] = x[lenght - 1 - i]
                y[lenght - i] = y[lenght - 1 - i]
                pygame.draw.rect(srf, clg, (x[i + 1], y[i + 1], 10, 10))
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


    def count(self):
        for i in x:
            self += 1
        return self
        pass


class food():
    def draw():
        pygame.draw.rect(srf, clr, (xF, yF, 10, 10))
        pass


    def add():
        global xF, yF, eaten
        xF = int(round(random.randint(1, W) / 100, 1) * 100)
        yF = int(round(random.randint(1, H) / 100, 1) * 100)
        eaten = False
        print(yF, xF)
        pass

    def eaten_check():
        if x[0] == xF and y[0] == yF:
            return True
        else:
            return False
            pass



def backwordsch(a,b):
    return a != b
    pass



def Border_Check_X(a):
    if a > BorderRIGHT:
        a = BorderLEFT
        return a
        breakpoint()
    if a < BorderLEFT:
        a = BorderRIGHT
    return a
    pass


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


def Border_Check_Y(a):
    if a > BorderDOWN + 10:
        a = BorderUP
        return a
        breakpoint()
    if a < BorderUP:
        a = BorderDOWN
    return a
    pass


FPS = 15
clock = pygame.time.Clock()
W, H = 400, 400
x = array('i', [W // 2, 0])
y = array('i', [H // 2, 0])
n = 0
m = 0

#colors
clg = (0, 255, 0)
clbl = (0, 0, 0)
clr = (255, 0, 0)
#______________________

srf = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")


BorderUP = BorderLEFT = 0
BorderDOWN = H
BorderRIGHT = W
speed = 10

moveX = 0
moveY = speed

eaten = True

xF = 0
yF = 0
xt = 0
yt = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    lenght = 0
    lenght = snake.count(lenght)
    snake.direction()
    if eaten:
        food.add()
    snake.move_head()


    if food.eaten_check():
        x.append(0)
        y.append(0)
        eaten = True

    srf.fill(clbl)
    snake.tail_build_and_draw()

    snake.draw()

    food.draw()
    pygame.display.update()
    clock.tick(FPS)
