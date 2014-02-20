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
        self.view  = camera.Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)


        pygame.display.set_caption("untitled_adventure_game")

        done = False

        clock = pygame.time.Clock()

        #sprite.groups
        all_sprites = pygame.sprite.Group()
        all_units = pygame.sprite.Group()

        #initiate player
        player = units.Hero(0,500,1,"Erick")
        all_sprites.add(player)
        all_units.add(player)

        #initiate enemies
        enemy = units.Enemy01(500,500,0)
        all_sprites.add(enemy)
        all_units.add(enemy)

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump(self.view.wall_list())
                    if event.key == pygame.K_SPACE:
                        player.attack()
                        all_units.add(player.attack_s)
                        all_sprites.add(player.attack_s)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.x_s < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.x_s > 0:
                        player.stop()

            # --- Game logic should go here
            all_sprites.add(self.view.wall_list())

            #player.update:
                #move all units
                    #check if hero slashed enemy
                    #update alive or death (kill necessaries)
                    #check if hero touched enemy (update health)
            player.update(all_sprites)

            # --- Drawing code should go here
            self.view.update(player, all_units)

            pygame.display.flip()

            clock.tick(10)

        pygame.quit()
