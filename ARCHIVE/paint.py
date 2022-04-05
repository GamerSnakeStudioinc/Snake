import pygame
pygame.init()

FPS = 30
clock = pygame.time.Clock()
W, H = 800, 800

#colors
clg = (0, 255, 0)
clbl = (0, 0, 0)
clr = (255, 0, 0)
#______________________

srf = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
pygame.display.update()

flSD = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flSD = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flSD:
                pos = event.pos

                w = pos[0] - sp[0]
                h = pos[1] - sp[1]

                srf.fill(clbl)
                pygame.draw.rect(srf, clg, pygame.Rect(sp[0], sp[1], w, h))
                pygame.display.update()
    clock.tick(FPS)