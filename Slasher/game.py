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


        #initiate player
        player = units.Hero(0,500,1,"Erick")
        all_sprites_list = pygame.sprite.Group()
        all_sprites_list.add(player)

        #initiate enemies
        enemy = units.Enemy01(500,500,0)
        all_sprites_list.add(enemy)

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
                        all_sprites_list.add(player.attack_s)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.x_s < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.x_s > 0:
                        player.stop()

            # --- Game logic should go here
            all_sprites_list.add(self.view.wall_list())
            player.update(all_sprites_list)
            enemy.update()

            # --- Drawing code should go here
            self.view.update(player, all_sprites_list)

            pygame.display.flip()

            clock.tick(10)

        pygame.quit()
