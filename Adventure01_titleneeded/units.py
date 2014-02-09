import spritesheet
import pygame
from constants import attack, colors, currentmap


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

    def move(self, objects):
        #up/down
        self.rect.y += self.y_s

        if(self.rect.y+attack.HERO_HEIGHT > currentmap.width):
            self.rect.y = currentmap.width-attack.HERO_HEIGHT
        elif(self.rect.y < 0):
            self.rect.y = 0

        #if hit walls
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for block in block_hit_list:
            if isinstance(block, Unit):
                if(block.sid == self.sid):
                    continue
                if isinstance(block, Enemy):
                    self.health -= 1
            if self.y_s > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        if self.y_s > 0: #going down
            if self.attacking:
                if self.cur_sprite == attack.HIT_DOWN2:
                    self.cur_sprite = attack.HIT_DOWN1
                else:
                    self.cur_sprite = attack.HIT_DOWN2
            elif self.cur_sprite == attack.WALK_DOWN2:
                self.cur_sprite = attack.WALK_DOWN1
            else:
                self.cur_sprite = attack.WALK_DOWN2

        if self.y_s < 0: #going up
            if self.attacking:
                if self.cur_sprite == attack.HIT_UP2:
                    self.cur_sprite = attack.HIT_UP1
                else:
                    self.cur_sprite = attack.HIT_UP2
            elif self.cur_sprite == attack.WALK_UP2:
                self.cur_sprite = attack.WALK_UP1
            else:
                self.cur_sprite = attack.WALK_UP2

        #left/right
        self.rect.x += self.x_s

        if(self.rect.x+attack.HERO_WIDTH > currentmap.height):
            self.rect.x = currentmap.height-attack.HERO_WIDTH
        elif(self.rect.x < 0):
            self.rect.x = 0

        if self.x_s > 0: #going right
            if self.attacking:
                if self.cur_sprite == attack.HIT_RIGHT2:
                    self.cur_sprite = attack.HIT_RIGHT1
                else:
                    self.cur_sprite = attack.HIT_RIGHT2
            elif self.cur_sprite == attack.WALK_RIGHT2:
                self.cur_sprite = attack.WALK_RIGHT1
            else:
                self.cur_sprite = attack.WALK_RIGHT2

        if self.x_s < 0: #going left
            if self.attacking:
                if self.cur_sprite == attack.HIT_LEFT2:
                    self.cur_sprite = attack.HIT_LEFT1
                else:
                    self.cur_sprite = attack.HIT_LEFT2
            elif self.cur_sprite == attack.WALK_LEFT2:
                self.cur_sprite = attack.WALK_LEFT1
            else:
                self.cur_sprite = attack.WALK_LEFT2

        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for  block in block_hit_list:
            if isinstance(block, Unit):
                if(block.sid == self.sid):
                    continue
                if isinstance(block, Enemy):
                    self.health -= 1
            if self.x_s > 0: #going right
                self.rect.right = block.rect.left
            else: #going left
                self.rect.left = block.rect.right

        self.image = self.sprites[self.cur_sprite]

    def __init__(self, x,y, s_id, name):
        Unit.__init__(self,x,y,s_id)
        self.name = name
        self.health = 20

class Enemy(Unit):

    attacking = True

    def __init__(self,x,y,s_id):
        Unit.__init__(self,x,y,s_id)

class Enemy01(Enemy):

    def __init__(self,x,y,s_id):
        Enemy.__init__(self,x,y,s_id)
        self.health = 3
        self.name = "Enemy01"
