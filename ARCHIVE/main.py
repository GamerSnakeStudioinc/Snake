import pygame
pygame.init()

FPS = 30
clock = pygame.time.Clock()
W, H = 600, 400

#colors
clg = (0, 255, 0)
clbl = (255, 255, 255)
clr = (255, 0, 0)
#______________________

srf = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
pygame.display.update()

x = W / 2
y = H / 2
speed = 5

flL = flR = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flL = True
            elif event.key == pygame.K_RIGHT:
                flR = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flL = flR = False
    if flL:
        x -= speed
    if flR:
        x += speed
    srf.fill(clbl)
    pygame.draw.rect(srf, clg, (x, y, 10, 10))
    pygame.display.update()

    clock.tick(FPS)