import pygame
import maps
import walls
from constants import attack, const, currentmap, colors

class Camera(object):

    def setCamera(self, cx,cy):
        self.wcp_x = cx
        self.wcp_y = cy

    def wall_list(self):
        return self.world[self.cur_map].wall_list
    #world coord to camera coord
    def cameraTransform(self,wx,wy):
        return (wx-self.wcp_x, wy-self.wcp_y)
    #camera coord to world coord
    def cameraTransformInv(self,cx,cy):
        return (self.wcp_x+cx, self.wcp_y+cy)

    def update(self, hero, sprites):

        current_map = self.world[self.cur_map]
        cp_hero = self.cameraTransform(hero.rect.x,hero.rect.y)

        #if character is close to edge of walking box, redraw part of map

        #left edge
        if(cp_hero[0] < 300 ):
            self.wcp_x = hero.rect.x - 300

        #right edge
        if((self.width < current_map.width) and
            cp_hero[0]+attack.B_WIDTH > 500 ):
            self.wcp_x = hero.rect.x+attack.B_WIDTH - 500

        #upper edge
        if(cp_hero[1] < 240 ):
            self.wcp_y = hero.rect.y - 240

        #lower edge
        if((self.height < current_map.height) and
            cp_hero[1]+attack.B_HEIGHT > 400 ):
            self.wcp_y = hero.rect.y+attack.B_HEIGHT - 400

        #edgecases for camera
        if(self.wcp_x < 0):
            self.wcp_x = 0
        elif((self.width < current_map.width) and
                self.wcp_x+self.width > current_map.width):
            self.wcp_x = current_map.width-const.SCREEN_WIDTH

        if(self.wcp_y < 0):
            self.wcp_y = 0
        elif((self.height < current_map.height) and
                self.wcp_y+self.height > current_map.height):
            self.wcp_y = current_map.height-const.SCREEN_HEIGHT


        area = (self.wcp_x,self.wcp_y,self.width,self.height)

        #blit sprites
        current_map.sp.fill(colors.hotpink)
        sprites.draw(current_map.sp)

        #blit bg
        self.subscreen.blit(current_map.bg,(0,0),area)
        #blit floor
        self.subscreen.blit(current_map.fl,(0,0),area)

        #blit character(s)
        self.subscreen.blit(hero.image,(cp_hero[0],cp_hero[1]))
        #blit sprites
        self.subscreen.blit(current_map.sp,(0,0),area)


    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.wcp_x = 0
        self.wcp_y = 0
        self.subscreen = pygame.display.set_mode((w,h))
        self.world = []

        #load first map
        mapfile = "../../scroller01.tmx"
        map00 = maps.MapRenderer(mapfile)
        map00.renderSurfaces()
        currentmap.width = map00.width
        currentmap.height = map00.height
        #map00.sh1.set_alpha(125)
        #map00.sh2.set_alpha(125)

        #add map to world list
        self.cur_map = 0
        self.world.append(map00)

