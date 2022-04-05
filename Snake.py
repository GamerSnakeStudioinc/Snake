import pygame
import random
from array import *

pygame.init()
class snake(object):
    def move_head():
        inputs.arrows()
        global xt, yt
        xt = x[0]
        yt = y[0]
        x[0] += moveX
        y[0] += moveY
        x[0] = Border_Check_X(x[0])
        y[0] = Border_Check_Y(y[0])
    def tail_build():
        if len(x) > 2:
            for n in range(1, len(x) - 1):
                x[len(x) - n] = x[len(x) - n - 1]
                y[len(x) - n] = y[len(x) - n - 1]
                pygame.draw.rect(game_surface, SNAKE_BODY, (x[len(x) - n], y[len(x) - n], 10, 10))
        if len(x) > 1:
            x[1] = xt
            y[1] = yt
            pygame.draw.rect(game_surface, SNAKE_BODY, (x[1], y[1], 10, 10))

        pass
    def hit_check(a, b):
        for i in range(1, len(x) - 1):
            if a == x[i] and b == y[i]:
                return True
            pass
    def tail_draw():
            for n in range(1, len(x)):
                pygame.draw.rect(game_surface, SNAKE_BODY, (x[n], y[n], 10, 10))
    def draw_head():
        pygame.draw.rect(game_surface, SNAKE_BODY, (x[0], y[0], 10, 10))
        pass

class food(object):
    def eaten_check():
        if x[0] == xF and y[0] == yF or press[pygame.K_e]:
            return True
            pass
    def add():
        global xF, yF
        xF = yF = H_OF_GAME + W_OF_GAME + 1
        while snake.hit_check(xF, yF) or (xF % 10 != 0) or (yF % 10 != 0):
            xF = int(round(random.randint(1, W_OF_GAME - 10) / 100, 1) * 100)
            yF = int(round(random.randint(1, H_OF_GAME - 10) / 100, 1) * 100)
    def geting_eaten():
        global score
        if food.eaten_check():
            x.append(0)
            y.append(0)
            score = len(x) - 1
            food.add()
        pass
    def draw():
        pygame.draw.rect(game_surface, FOOD, (xF, yF, 10, 10))
        pass

class game():
    def cosplay_yarmongand():
        global score, x, y, moveX, moveY
        # Died screen fonts
        f_died_screen_text = pygame.font.Font("/home/jayanta/Python/GAme/minecraft.ttf", 40)
        died_screen_text = f_died_screen_text.render("You died!", 1, WHITE)
        died_screen_text_pos = died_screen_text.get_rect(center=(W_OF_SCREEN // 2, H_OF_SCREEN // 2 - H_OF_SCREEN // 10))

        f_died_screen_score = pygame.font.Font("/home/jayanta/Python/GAme/minecraft.ttf", 20)
        died_screen_score = f_died_screen_score.render('Score: ' + str(score), 1, WHITE)
        died_screen_score_pos = died_screen_score.get_rect(center=(W_OF_SCREEN // 2, died_screen_text_pos.bottom + 10))

        if snake.hit_check(x[0], y[0]):
            while True:
                r = 0 # Gotta cut out
                press = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or press[pygame.K_ESCAPE]:
                        pygame.quit()
                        exit()
                    if press[pygame.K_r]:
                        r = 1 # Gotta cut out
                if r == 1:
                    x = array('i', [W_OF_GAME // 2])
                    y = array('i', [H_OF_GAME // 2])
                    break
                died_screen.fill((255, 0, 0))
                died_screen.set_alpha(60)
                window.blit(game_surface, (0, 0))
                window.blit(score_text, score_pos)
                window.blit(died_screen, (0, 0))
                window.blit(died_screen_text, died_screen_text_pos)
                window.blit(died_screen_score, died_screen_score_pos)
                pygame.display.update()
        pass

class inputs():
    def arrows():
        global moveY, moveX
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


# Game settings
W_OF_SCREEN, H_OF_SCREEN = 800, 600
FPS = 15
clock = pygame.time.Clock()
speed = 10

# Var
xt = 0
yt = 0
moveX = 0
moveY = speed
score = 0

# Window
window = pygame.display.set_mode((W_OF_SCREEN, H_OF_SCREEN))
pygame.display.set_icon(pygame.image.load("Icon.png"))
pygame.display.set_caption("SnakeV0.4")

# colors
SNAKE_BODY = (139, 69, 19)
FIELD = (245, 222, 179)
FOOD = (255, 69, 0)
WHITE = (255, 255, 255)

# Game surface
W_OF_GAME, H_OF_GAME = W_OF_SCREEN, H_OF_SCREEN
game_surface = pygame.Surface((W_OF_GAME, H_OF_GAME))
BorderUP = BorderLEFT = 0
BorderDOWN = H_OF_GAME
BorderRIGHT = W_OF_GAME

# Died screen surface
died_screen = pygame.Surface((W_OF_SCREEN, H_OF_SCREEN))


# Arrays
x = array('i', [W_OF_GAME // 2])
y = array('i', [H_OF_GAME // 2])


# Score fonts
f_score = pygame.font.SysFont("loma", 20)
score_text = f_score.render('Score: ' + str(score), 1, FOOD)
score_pos = score_text.get_rect(center=(W_OF_SCREEN - 50, 10))

food.add()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    press = pygame.key.get_pressed()

    snake.move_head()
    snake.tail_build()
    game.cosplay_yarmongand()
    food.geting_eaten()

    game_surface.fill(FIELD)
    snake.draw_head()
    snake.tail_draw()
    food.draw()
    window.blit(game_surface, (0, 0))
    score_text = f_score.render('Score: ' + str(len(x) - 1), 1, FOOD, FIELD)
    window.blit(score_text, score_pos)
    pygame.display.update()
    clock.tick(FPS)