import pygame

pygame.init()
class pos:
    def __init__(self, x, y):
        self.pos = x, y
        self.pos_x = x
        self.pos_y = y
    def set_pos(self, new_x, new_y):
        self.pos = new_x, new_y
    def print_pos(self):
        print("Position: %s, %s" % self.pos)
W_OF_SCREEN, H_OF_SCREEN = 600, 400

sc = pygame.display.set_mode((W_OF_SCREEN, H_OF_SCREEN))
pygame.display.set_caption("Snake")

#colors
GREEN = (139, 69, 19)
BLACK = (245, 222, 179)
RED = (255, 69, 0)
WHITE = (255, 255, 255)
#______________________

FPS = 60
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    food_pos = pos(0, 0)
    food_pos.set_pos(19, 19)
    food_pos.print_pos()
    food = pygame.Rect((food_pos.pos_x, food_pos.pos_y), 10, 10)
    pygame.draw.rect(sc, RED, food)
    pygame.display.update()
    clock.tick(FPS)