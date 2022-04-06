import pygame
import random
from array import *
# v 0.5.0
pygame.init()
class snake(object):
    def move_head():
        inputs.arrows()
        global x_temperal, y_temperal
        x_temperal = snake_x[0]
        y_temperal = snake_y[0]
        snake_x[0] += moveX
        snake_y[0] += moveY
        snake_x[0] = Border_Check_X(snake_x[0])
        snake_y[0] = Border_Check_Y(snake_y[0])
    def tail_build():
        if len(snake_x) > 2:
            for n in range(1, len(snake_x) - 1):
                snake_x[len(snake_x) - n] = snake_x[len(snake_x) - n - 1]
                snake_y[len(snake_x) - n] = snake_y[len(snake_x) - n - 1]
        if len(snake_x) > 1:
            snake_x[1] = x_temperal
            snake_y[1] = y_temperal

        pass
    def hit_check(a, b):
        for i in range(1, len(snake_x) - 1):
            if a == snake_x[i] and b == snake_y[i]:
                return True
            pass
    def tail_draw():
            for n in range(1, len(snake_x)):
                pygame.draw.rect(game_surface, SNAKE_BODY_COLOR, (snake_x[n], snake_y[n], 10, 10))
    def draw_head():
        pygame.draw.rect(game_surface, SNAKE_BODY_COLOR, (snake_x[0], snake_y[0], 10, 10))
        pass

class food(object):
    def eaten_check():
        if snake_x[0] == food_x and snake_y[0] == food_y or press[pygame.K_e]:
            return True
            pass
    def add():
        global food_x, food_y
        food_x = food_y = H_OF_GAME + W_OF_GAME + 1
        while snake.hit_check(food_x, food_y) or (food_x % 10 != 0) or (food_y % 10 != 0):
            food_x = int(round(random.randint(1, W_OF_GAME - 10) / 100, 1) * 100)
            food_y = int(round(random.randint(1, H_OF_GAME - 10) / 100, 1) * 100)
    def geting_eaten():
        global score
        if food.eaten_check():
            snake_x.append(0)
            snake_y.append(0)
            score = len(snake_x) - 1
            food.add()
        pass
    def draw():
        pygame.draw.rect(game_surface, FOOD_COLOR, (food_x, food_y, 10, 10))
        pass

class game():
    def cosplay_yarmongand():
        global score, snake_x, snake_y, moveX, moveY

        if snake.hit_check(snake_x[0], snake_y[0]):
            # Died screen fonts
            f_died_screen_text = pygame.font.Font("/home/jayanta/Python/GAme/minecraft.ttf", 40)
            died_screen_text = f_died_screen_text.render("You died!", 1, WHITE)
            died_screen_text_pos = died_screen_text.get_rect(center=(W_OF_SCREEN // 2, H_OF_SCREEN // 2 - H_OF_SCREEN // 10))
            died_screen_text_shadow = f_died_screen_text.render("You died!", 1, BLACK)
            died_screen_text_shadow_pos = died_screen_text.get_rect(center=(W_OF_SCREEN // 2 + 3, H_OF_SCREEN // 2 - H_OF_SCREEN // 10 + 3))
            died_screen_text_shadow.set_alpha(170)

            f_died_screen_score_text = pygame.font.Font("/home/jayanta/Python/GAme/minecraft.ttf", 20)
            died_screen_score_text = f_died_screen_score_text.render('Score: ', 1, WHITE)
            died_screen_score_text_pos = died_screen_score_text.get_rect(center=(W_OF_SCREEN // 2, died_screen_text_pos.bottom + 10))
            died_screen_score_text_shadow = f_died_screen_score_text.render('Score: ' + str(score), 1, BLACK)
            died_screen_score_text_shadow_pos = died_screen_score_text.get_rect(center=(W_OF_SCREEN // 2 + 2, died_screen_text_pos.bottom + 10 + 2))
            died_screen_score_text_shadow.set_alpha(200)

            died_screen_score = f_died_screen_score_text.render(str(score), 1, DIED_SCREEN_SCORE_COLOR)
            died_screen_score_pos = died_screen_score.get_rect(topleft=died_screen_score_text_pos.topright)
            died_screen_score_pos.move_ip(0, 1)

            f_died_screen_buttons = pygame.font.Font("/home/jayanta/Python/GAme/minecraft.ttf", 15)
            died_screen_buttons = f_died_screen_buttons.render('Press "R" to restart', 1, WHITE)
            died_screen_buttons_pos = died_screen_buttons.get_rect(center=(W_OF_SCREEN // 2, died_screen_score_text_pos.bottom + 30))
            died_screen_buttons_shadow = f_died_screen_buttons.render('Press "R" to restart', 1, BLACK)
            died_screen_buttons_shadow_pos = died_screen_buttons.get_rect(
                center=(W_OF_SCREEN // 2 + 2, died_screen_score_text_pos.bottom + 30 + 2))
            died_screen_buttons_shadow.set_alpha(200)
            while True:
                press = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or press[pygame.K_ESCAPE]:
                        pygame.quit()
                        exit()
                if press[pygame.K_r]:
                    snake_x = array('i', [W_OF_GAME // 2])
                    snake_y = array('i', [H_OF_GAME // 2])
                    moveX = 0
                    moveY = speed
                    food.add()
                    break
                died_screen.fill((255, 0, 0))
                died_screen.set_alpha(60)
                window.blit(game_surface, (0, 0))
                window.blit(score_text, score_pos)
                window.blit(died_screen, (0, 0))
                window.blit(died_screen_text_shadow, died_screen_text_shadow_pos)
                window.blit(died_screen_text, died_screen_text_pos)
                window.blit(died_screen_score_text_shadow, died_screen_score_text_shadow_pos)
                window.blit(died_screen_score, died_screen_score_pos)
                # window.blit(died_screen_score_shadow, died_screen_score_shadow_pos)
                window.blit(died_screen_score_text, died_screen_score_text_pos)
                window.blit(died_screen_buttons_shadow, died_screen_buttons_shadow_pos)
                window.blit(died_screen_buttons, died_screen_buttons_pos)
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
x_temperal = 0
y_temperal = 0
moveX = 0
moveY = speed
score = 0

# Window
window = pygame.display.set_mode((W_OF_SCREEN, H_OF_SCREEN))
pygame.display.set_icon(pygame.image.load("Icon.png"))
pygame.display.set_caption("SnakeV0.4")

# colors
SNAKE_BODY_COLOR = (139, 69, 19)
FIELD_COLOR = (245, 222, 179)
FOOD_COLOR = (255, 69, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIED_SCREEN_SCORE_COLOR = (247, 246, 96)
# Game surface
W_OF_GAME, H_OF_GAME = W_OF_SCREEN, H_OF_SCREEN
game_surface = pygame.Surface((W_OF_GAME, H_OF_GAME))
BorderUP = BorderLEFT = 0
BorderDOWN = H_OF_GAME
BorderRIGHT = W_OF_GAME

# Died screen surface
died_screen = pygame.Surface((W_OF_SCREEN, H_OF_SCREEN))


# Arrays
snake_x = array('i', [W_OF_GAME // 2])
snake_y = array('i', [H_OF_GAME // 2])


# Score fonts
f_score = pygame.font.SysFont("loma", 20)
score_text = f_score.render('Score: ' + str(score), 1, FOOD_COLOR)

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

    game_surface.fill(FIELD_COLOR)
    snake.draw_head()
    snake.tail_draw()
    food.draw()
    window.blit(game_surface, (0, 0))
    score_pos = score_text.get_rect(center=(W_OF_SCREEN - 50, 10))
    score_text = f_score.render('Score: ' + str(len(snake_x) - 1), 1, FOOD_COLOR)
    window.blit(score_text, score_pos)
    pygame.display.update()
    clock.tick(FPS)