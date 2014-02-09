import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
beige    = ( 222, 226, 192)

w = 640
h = 480

size = (w,h)

pygame.init()

size = (w,h)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("untitled_adventure_game")

subscreen = pygame.Surface((w,h))
subscreen.fill(green)

surf = pygame.Surface((w,h))
surf.fill(red)

larea = (0,0,50,50)
sarea = (0,0,25,25)
carea = (9,9, 26,26)
screen.blit(surf,(0,0),larea)
screen.blit(subscreen, (10,10),sarea)

screen.set_colorkey(red)
screen.blit(screen,(50,50),carea)

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pygame.display.flip()
    clock.tick(10)

pygame.quit()