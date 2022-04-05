import pygame
pygame.init()

def BorderCHX(a):
    a = (BorderLEFT + 10) if (a == BorderRIGHT) else a
    a = (BorderRIGHT - 10) if (a == BorderLEFT) else a
    return a
def BorderCHY(b):
    b = (BorderUP + 10) if (b == BorderDOWN) else b
    b = (BorderDOWN - 10) if (b == BorderUP) else b
    return b
FPS = 30
clock = pygame.time.Clock()
W, H = 600, 600

#colors
clg = (0, 255, 0)
clbl = (0, 0, 0)
clr = (255, 0, 0)
#______________________

srf = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
pygame.display.update()

x = W // 2
y = H // 2

BorderUP = BorderLEFT = 0
BorderDOWN = W
BorderRIGHT = H
speed = 10

moveX = 0
moveY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    press = pygame.key.get_pressed()
    if press[pygame.K_LEFT]:
        moveX = -speed
        moveY = 0
    if press[pygame.K_RIGHT]:
        moveX = speed
        moveY = 0
    if press[pygame.K_UP]:
        moveY = -speed
        moveX = 0
    if press[pygame.K_DOWN]:
        moveY = speed
        moveX = 0
    x += moveX
    y += moveY
    x = BorderCHX(x)
    y = BorderCHY(y)
    srf.fill(clbl)
    pygame.draw.rect(srf, clg, (x, y, 10, 10))
    pygame.display.update()

    clock.tick(FPS)