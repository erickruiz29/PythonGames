import pygame
import walls
from constants import colors, layers
from pygame.locals import *
import math, glob

class MapRenderer(object):
    """
    Super simple way to render a tiled map
    """

    def __init__(self, filename):
        from pytmx import tmxloader
        self.tiledmap = tmxloader.load_pygame(filename, pixelalpha=True)
        self.wall_list = pygame.sprite.Group()

        self.width = self.tiledmap.width * self.tiledmap.tilewidth
        self.height = self.tiledmap.height * self.tiledmap.tileheight

        self.bg  = pygame.Surface((self.width,self.height))
        self.fl  = pygame.Surface((self.width,self.height))
        self.sp  = pygame.Surface((self.width,self.height))
        #self.fg  = pygame.Surface((self.width,self.height))
        self.tp  = pygame.Surface((self.width,self.height))
        #self.sh1 = pygame.Surface((self.width,self.height))
        #self.sh2 = pygame.Surface((self.width,self.height))


        self.fl.fill(colors.hotpink)
        self.sp.fill(colors.hotpink)
        #self.fg.fill(colors.hotpink)
        self.tp.fill(colors.hotpink)
        #self.sh1.fill(colors.hotpink)
        #self.sh2.fill(colors.hotpink)
        self.fl.set_colorkey(colors.hotpink)
        self.sp.set_colorkey(colors.hotpink)
        #self.fg.set_colorkey(colors.hotpink)
        self.tp.set_colorkey(colors.hotpink)
        #self.sh1.set_colorkey(colors.hotpink)
        #self.sh2.set_colorkey(colors.hotpink)


    def renderSurfaces(self):
        # not going for efficiency here
        # for demonstration purposes only

        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.getTileImage

        # draw map tiles
        for l in xrange(0, len(self.tiledmap.tilelayers)):
            for y in xrange(0, self.tiledmap.height):
                for x in xrange(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    tGid = self.tiledmap.getTileGID(x,y,l)
                    if tile and (not tGid == 0) and l==layers.background:
                        self.bg.blit(tile, (x*tw, y*th))
                    if tile and (not tGid == 0) and l==layers.floor:
                        self.fl.blit(tile,(x*tw, y*th))


        # add obstructions to wall list
        bl = pygame.Surface((self.width,self.height))
        for og in self.tiledmap.objectgroups:
            for o in og:
                wall = walls.Wall(o.x,o.y,o.width,o.height,(0,0,0))
                self.wall_list.add(wall)
