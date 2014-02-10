import spritesheet
import pygame
from constants import attack, colors, currentmap, dirs, const
from random import randrange


class Unit(pygame.sprite.Sprite):

    cur_sprite = 0
    x_s = 0
    y_s = 0

    def load_sprite(self, sheet):
        index = 0
        if(self.sid>100):
            index = self.sid-100
        else:
            index = self.sid
        c = (index%5)
        r = (index//5)
        cw,ch,bw,bh=(0,0,0,0)

        if sheet.name == "img/attack.gif":
            cw = attack.C_WIDTH
            ch = attack.C_HEIGHT
            bw = attack.B_WIDTH
            bh = attack.B_HEIGHT
            self.width = attack.B_WIDTH
            self.height = attack.B_HEIGHT

        for sr in range(4):
            for sc in range(4):
                left = ((((4*c)+sc)*cw)+1)
                top = ((((4*r)+sr)*ch)+2)

                rect = pygame.Rect(left,top,bw,bh)
                sprite = sheet.image_at(rect,colors.beige)
                twice = pygame.transform.scale2x(sprite)
                self.sprites.append(twice)

    def changespeed(self, x, y):
        self.x_s += x
        self.y_s += y

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.y_s == 0:
            self.y_s = 7
        else:
            self.y_s += 5

        # See if we are on the ground.
        if self.rect.y >= const.SCREEN_WIDTH - self.rect.height and self.y_s >= 0:
            self.change_y = 0
            self.rect.y = const.SCREEN_HEIGHT - self.rect.height


    def __init__(self, x,y, s_id):
        self.sheet = spritesheet.Spritesheet('img/attack.gif')
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sid = s_id
        self.load_sprite(self.sheet)
        self.cur_sprite = 0
        self.image = self.sprites[self.cur_sprite]

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.width = 0
        self.height = 0

class Hero(Unit):

    attacking = False

    def stop(self):
        self.x_s = 0

    def go_right(self):
        self.x_s = 10

    def go_left(self):
        self.x_s = -10

    def attack(self):
        if(self.attack_timer == 0):
            self.attack_timer = 9


    def jump(self, objects):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, objects, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= const.SCREEN_HEIGHT:
            self.y_s = -35

    def update(self, objects):
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.x_s

        #check map edges
        if(self.rect.x+self.rect.width > currentmap.width):
            self.rect.x = currentmap.width-self.rect.width
        elif(self.rect.x < 0):
            self.rect.x = 0

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for block in block_hit_list:
            if isinstance(block, Unit):
                if(block.sid == self.sid):
                    continue
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.x_s > 0:
                self.rect.right = block.rect.left
            elif self.x_s < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.y_s

        if(self.rect.y+self.rect.height > currentmap.height):
            self.rect.y = currentmap.height-self.rect.height
        elif(self.rect.y < 0):
            self.rect.y = 0

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for block in block_hit_list:
            if isinstance(block, Unit):
                if(block.sid == self.sid):
                    continue
            # Reset our position based on the top/bottom of the object.
            if self.y_s > 0:
                self.rect.bottom = block.rect.top
            elif self.y_s < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.y_s = 0

        #attack
        if(self.attack_timer > 0):
            self.attack_timer -= 1
            self.attack_s.rect.x = self.rect.x+self.rect.width
            self.attack_s.rect.y = self.rect.y
        if(self.attack_timer == 9):
            objects.add(self.attack_s)
        if(self.attack_timer == 0):
            self.attack_s.kill()
        self.attack_s.update(objects)


    def __init__(self, x,y, s_id, name):
        Unit.__init__(self,x,y,s_id)
        self.name = name
        self.health = 20
        sl = Slash(self.rect.x+self.rect.width,self.rect.y)
        self.attack_s = sl
        self.attack_timer = 0

class Enemy(Unit):

    def __init__(self,x,y,s_id):
        Unit.__init__(self,x,y,s_id)

class Enemy01(Enemy):

    def update(self):
        if(self.health <= 0):
            self.kill()
        print(self.health)

    def __init__(self,x,y,s_id):
        Enemy.__init__(self,x,y,s_id)
        self.health = 10
        self.name = "Enemy01"

class Slash(pygame.sprite.Sprite):

    def update(self, objects):
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for block in block_hit_list:
            if(isinstance(block,Enemy)):
                block.health -= 1 #add a funct to make it move back

    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, attack.HERO_HEIGHT])
        self.image.fill(colors.blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y