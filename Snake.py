import pygame
import random
from array import *
# v 0.5.0
pygame.init()
class snake:
    def move_head():
        inputs.arrows()
        global x_temporal, y_temporal
        x_temporal = snake_x[0]
        y_temporal = snake_y[0]
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
            snake_x[1] = x_temporal
            snake_y[1] = y_temporal

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

class food:
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

class game:
    def menu():
        global menu_status, SNAKE_BODY_COLOR, FOOD_COLOR, FIELD_COLOR, H_OF_SCREEN, W_OF_SCREEN, W_OF_GAME, H_OF_GAME, BorderRIGHT, BorderDOWN, window, game_surface
        f_menu_game_name = pygame.font.Font("QuicksilverFastRegular.ttf", 60)
        f_menu_game_start = pygame.font.Font("GvTimeRegular.ttf", 30)
        while True:
            press = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if press[pygame.K_SPACE]:
                menu_status = False
                break
            menu_game_name = f_menu_game_name.render("SNAKE", 1, FOOD_COLOR)
            menu_game_name_pos = menu_game_name.get_rect(
                center=(W_OF_GAME // 2, H_OF_GAME // 2 - H_OF_GAME // 10))

            menu_game_start = f_menu_game_start.render('Press "Spase" to start', 1, FOOD_COLOR)
            menu_game_start_pos = menu_game_start.get_rect(center=(W_OF_GAME // 2, menu_game_name_pos.bottom + 20))
            game_surface.fill(FIELD_COLOR)
            window.blit(game_surface, (0, 0))
            window.blit(menu_game_name, menu_game_name_pos)
            window.blit(menu_game_start, menu_game_start_pos)
            if press[pygame.K_ESCAPE]:
                exit = pygame.Surface((W_OF_GAME//3, H_OF_GAME//3))
                exit_pos = exit.get_rect(center=(W_OF_GAME//2, H_OF_GAME//2))
                exit.fill(BLACK)
                f_exit_text = pygame.font.Font("BiggestGarbage.otf", 20)
                exit_text = f_exit_text.render("Do you want to leave? y/n", 1, WHITE)
                exit_text_pos = exit_text.get_rect(center=exit_pos.center)
                window.blit(exit, exit_pos)
                window.blit(exit_text, exit_text_pos)
                pygame.display.update()
                while True:
                    press = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if press[pygame.K_y]:
                        exit()
                    if press[pygame.K_n]:
                        break
            if press[pygame.K_d]:
                difficult = pygame.Surface((W_OF_GAME // 3, H_OF_GAME // 3))
                difficult_pos = difficult.get_rect(center=(W_OF_GAME // 2, H_OF_GAME // 2))
                difficult.fill(BLACK)
                f_difficult_text = pygame.font.Font("BiggestGarbage.otf", 20)
                difficult_text = f_difficult_text.render("Difficult: 1-3", 1, WHITE)
                difficult_text_pos = difficult_text.get_rect(center=difficult_pos.center)
                window.blit(difficult, difficult_pos)
                window.blit(difficult_text, difficult_text_pos)
                pygame.display.update()
                while True:
                    global FPS
                    press = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if press[pygame.K_0]:
                        FPS = 7
                        break
                    if press[pygame.K_1]:
                        FPS = 10
                        break
                    if press[pygame.K_2]:
                        FPS = 15
                        break
                    if press[pygame.K_3]:
                        FPS = 25
                        break
            if press[pygame.K_t]:
                theme = pygame.Surface((W_OF_GAME // 3, H_OF_GAME // 3))
                theme_pos = theme.get_rect(center=(W_OF_GAME // 2, H_OF_GAME // 2))
                theme.fill(BLACK)
                f_theme_text = pygame.font.Font("BiggestGarbage.otf", 20)
                theme_text = f_theme_text.render("Theme: 1-9", 1, WHITE)
                theme_text_pos = theme_text.get_rect(center=theme_pos.center)
                window.blit(theme, theme_pos)
                window.blit(theme_text, theme_text_pos)
                pygame.display.update()
                while True:
                    press = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if press[pygame.K_0]:
                        SNAKE_BODY_COLOR = (0, 255, 0)
                        FIELD_COLOR = BLACK
                        FOOD_COLOR = (255, 0, 0)
                        break
                    if press[pygame.K_1]:
                        SNAKE_BODY_COLOR = BLACK
                        FIELD_COLOR = (243, 202, 32)
                        FOOD_COLOR = BLACK
                        break
                    if press[pygame.K_2]:
                        SNAKE_BODY_COLOR = (207, 184, 69)
                        FIELD_COLOR = (20, 20, 20)
                        FOOD_COLOR = (127, 195, 192)
                        break
                    if press[pygame.K_3]:
                        SNAKE_BODY_COLOR = (69, 118, 235)
                        FIELD_COLOR = (163, 210, 71)
                        FOOD_COLOR = (232, 69, 23)
                        break
                    if press[pygame.K_4]:
                        SNAKE_BODY_COLOR = (78, 59, 48)
                        FIELD_COLOR = (168, 135, 109)
                        FOOD_COLOR = (66, 58, 52)
                        break
                    if press[pygame.K_5]:
                        SNAKE_BODY_COLOR = (0, 10, 20)
                        FIELD_COLOR = (137, 156, 114)
                        FOOD_COLOR = (0, 10, 20)
                        break
                    if press[pygame.K_6]:
                        SNAKE_BODY_COLOR = (139, 69, 19)
                        FIELD_COLOR = (245, 222, 179)
                        FOOD_COLOR = (255, 69, 0)
                        break
                    if press[pygame.K_ESCAPE]:
                        break
            if press[pygame.K_s]:
                resolution = pygame.Surface((W_OF_GAME // 3, H_OF_GAME // 3))
                resolution_pos = resolution.get_rect(center=(W_OF_GAME // 2, H_OF_GAME // 2))
                resolution.fill(BLACK)
                f_resolution_text = pygame.font.Font("BiggestGarbage.otf", 20)
                resolution_text = f_resolution_text.render("Resolution: 1-4", 1, WHITE)
                resolution_text_pos = resolution_text.get_rect(center=resolution_pos.center)
                window.blit(resolution, resolution_pos)
                window.blit(resolution_text, resolution_text_pos)
                pygame.display.update()
                while True:
                    press = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if press[pygame.K_0]:
                        W_OF_SCREEN = 200
                        H_OF_SCREEN = 200
                        break
                    if press[pygame.K_1]:
                        W_OF_SCREEN = 400
                        H_OF_SCREEN = 200
                        break
                    if press[pygame.K_2]:
                        W_OF_SCREEN = 600
                        H_OF_SCREEN = 400
                        break
                    if press[pygame.K_3]:
                        W_OF_SCREEN = 800
                        H_OF_SCREEN = 600
                        break
                    if press[pygame.K_4]:
                        W_OF_SCREEN = 1250
                        H_OF_SCREEN = 640
                        break
                window = pygame.display.set_mode((W_OF_SCREEN, H_OF_SCREEN))
                W_OF_GAME, H_OF_GAME = W_OF_SCREEN, H_OF_SCREEN
                game_surface = pygame.Surface((W_OF_GAME, H_OF_GAME))
                BorderDOWN = H_OF_GAME
                BorderRIGHT = W_OF_GAME
                food.add()
            if press[pygame.K_ESCAPE]:
                exit = pygame.Surface((W_OF_GAME//3, H_OF_GAME//3))
                exit_pos = exit.get_rect(center=(W_OF_GAME//2, H_OF_GAME//2))
                exit.fill(BLACK)
                f_exit_text = pygame.font.Font("BiggestGarbage.otf", 20)
                exit_text = f_exit_text.render("Do you want to leave? y/n", 1, WHITE)
                exit_text_pos = exit_text.get_rect(center=exit_pos.center)
                window.blit(exit, exit_pos)
                window.blit(exit_text, exit_text_pos)
                pygame.display.update()
                while True:
                    press = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if press[pygame.K_y]:
                        exit()
                    if press[pygame.K_n]:
                        break


            pygame.display.update()
    def reset_if_hit():
        global score, snake_x, snake_y, moveX, moveY

        if snake.hit_check(snake_x[0], snake_y[0]):
            snake_x = array('i', [W_OF_GAME // 2])
            snake_y = array('i', [H_OF_GAME // 2])
            moveX = 0
            moveY = speed
            # Died screen fonts
            f_died_screen_text = pygame.font.Font("minecraft.ttf", 40)
            died_screen_text = f_died_screen_text.render("You died!", 1, WHITE)
            died_screen_text_pos = died_screen_text.get_rect(center=(W_OF_GAME // 2, H_OF_GAME // 2 - H_OF_GAME // 10))
            died_screen_text_shadow = f_died_screen_text.render("You died!", 1, BLACK)
            died_screen_text_shadow_pos = died_screen_text.get_rect(center=(W_OF_GAME // 2 + 3, H_OF_GAME // 2 - H_OF_GAME // 10 + 3))
            died_screen_text_shadow.set_alpha(170)

            f_died_screen_score_text = pygame.font.Font("minecraft.ttf", 20)
            died_screen_score_text = f_died_screen_score_text.render('Score: ', 1, WHITE)
            died_screen_score_text_pos = died_screen_score_text.get_rect(center=(W_OF_GAME // 2, died_screen_text_pos.bottom + 10))
            died_screen_score_text_shadow = f_died_screen_score_text.render('Score: ' + str(score), 1, BLACK)
            died_screen_score_text_shadow_pos = died_screen_score_text.get_rect(center=(W_OF_GAME // 2 + 2, died_screen_text_pos.bottom + 10 + 2))
            died_screen_score_text_shadow.set_alpha(200)

            died_screen_score = f_died_screen_score_text.render(str(score), 1, DIED_SCREEN_SCORE_COLOR)
            died_screen_score_pos = died_screen_score.get_rect(topleft=died_screen_score_text_pos.topright)
            died_screen_score_pos.move_ip(0, 1)

            f_died_screen_buttons = pygame.font.Font("minecraft.ttf", 15)
            died_screen_buttons = f_died_screen_buttons.render('Press "R" to restart', 1, WHITE)
            died_screen_buttons_pos = died_screen_buttons.get_rect(center=(W_OF_GAME // 2, died_screen_score_text_pos.bottom + 30))
            died_screen_buttons_shadow = f_died_screen_buttons.render('Press "R" to restart', 1, BLACK)
            died_screen_buttons_shadow_pos = died_screen_buttons.get_rect(
                center=(W_OF_GAME // 2 + 2, died_screen_score_text_pos.bottom + 30 + 2))
            died_screen_buttons_shadow.set_alpha(200)
            while True:
                press = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                if press[pygame.K_r]:
                    food.add()
                    break

                if press[pygame.K_ESCAPE]:
                    menu_status = True
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

class inputs:
    def arrows():
        global moveY, moveX
        if press[pygame.K_LEFT] and backwordsch(moveX, speed):
            moveX = -speed
            moveY = 0
            return
        if press[pygame.K_RIGHT] and backwordsch(moveX, -speed):
            moveX = speed
            moveY = 0
            return
        if press[pygame.K_UP] and backwordsch(moveY, speed):
            moveY = -speed
            moveX = 0
            return
        if press[pygame.K_DOWN] and backwordsch(moveY, -speed):
            moveY = speed
            moveX = 0
            return
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
x_temporal = 0
y_temporal = 0
moveX = 0
moveY = speed
score = 0

# Window
window = pygame.display.set_mode((W_OF_SCREEN, H_OF_SCREEN))
pygame.display.set_icon(pygame.image.load("Icon.png"))
pygame.display.set_caption("SnakeV0.4")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SNAKE_BODY_COLOR = (0, 255, 0)
FIELD_COLOR = BLACK
FOOD_COLOR = (255, 0, 0)
DIED_SCREEN_SCORE_COLOR = (247, 246, 96)
# Game surface
W_OF_GAME, H_OF_GAME = W_OF_SCREEN, H_OF_SCREEN
game_surface = pygame.Surface((W_OF_GAME, H_OF_GAME))
BorderUP = BorderLEFT = 0
BorderDOWN = H_OF_GAME
BorderRIGHT = W_OF_GAME

# Died screen surface
died_screen = pygame.Surface((W_OF_GAME, H_OF_GAME))


# Arrays
snake_x = array('i', [W_OF_GAME // 2])
snake_y = array('i', [H_OF_GAME // 2])


# Score fonts
f_score = pygame.font.SysFont("loma", 20)
score_text = f_score.render('Score: ' + str(score), 1, FOOD_COLOR)

food.add()
menu_status = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    press = pygame.key.get_pressed()
    if press[pygame.K_ESCAPE]:
        menu_status = True
    snake.move_head()
    food.geting_eaten()
    snake.tail_build()
    game.reset_if_hit()
    if menu_status:
        game.menu()
    game_surface.fill(FIELD_COLOR)
    snake.draw_head()
    snake.tail_draw()
    food.draw()
    window.blit(game_surface, (0, 0))
    score_pos = score_text.get_rect(center=(W_OF_GAME - 50, 10))
    score_text = f_score.render('Score: ' + str(len(snake_x) - 1), 1, FOOD_COLOR)
    window.blit(score_text, score_pos)
    pygame.display.update()
    clock.tick(FPS)