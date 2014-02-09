import pygame
import units
import camera
from constants import const, colors

class Game(object):


    def __init__(self):
        self.g=0

    def run(self):
        pygame.init()

        #start camera
        self.view  = camera.Camera(const.screen_width, const.screen_height)


        pygame.display.set_caption("untitled_adventure_game")

        done = False

        clock = pygame.time.Clock()


        #initiate player
        player = units.Hero(300,500,1,"Erick")


        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(-10,0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(10,0)
                    if event.key == pygame.K_UP:
                        player.changespeed(0,-10)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0,10)
                    if event.key == pygame.K_SPACE:
                        player.attacking = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(10,0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(-10,0)
                    if event.key == pygame.K_UP:
                        player.changespeed(0,10)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0,-10)
                    if event.key == pygame.K_SPACE:
                        player.attacking = False

            # --- Game logic should go here
            player.move(self.view.wall_list())

            # --- Drawing code should go here
            self.view.update(player)

            pygame.display.flip()

            clock.tick(10)

        pygame.quit()
