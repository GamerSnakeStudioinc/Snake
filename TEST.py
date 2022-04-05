import pygame

pygame.init()

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

    clock.tick(FPS)