"""Game constants"""

class colors(object):
    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    beige    = ( 222, 226, 192)
    hotpink  = ( 255,   0, 180)
    blue     = (   0,   0, 255)
    purple   = ( 255,   0, 255)

class attack(object):
    WALK_UP1    = 0
    WALK_UP2    = 1
    HIT_UP1     = 2
    HIT_UP2     = 3
    WALK_RIGHT1 = 4
    WALK_RIGHT2 = 5
    HIT_RIGHT1  = 6
    HIT_RIGHT2  = 7
    WALK_DOWN1  = 8
    WALK_DOWN2  = 9
    HIT_DOWN1   = 10
    HIT_DOWN2   = 11
    WALK_LEFT1  = 12
    WALK_LEFT2  = 13
    HIT_LEFT1   = 14
    HIT_LEFT2   = 15
    C_WIDTH     = 18
    C_HEIGHT    = 20
    B_WIDTH     = 14
    B_HEIGHT    = 18
    HERO_WIDTH  = 28
    HERO_HEIGHT = 36

class const(object):
    SCREEN_WIDTH    = 800
    SCREEN_HEIGHT   = 640

class currentmap(object):
    width   = 0
    height  = 0

class layers(object):
    background = 0
    floor      = 1

class dirs(object):
    left    = 0
    right   = 1
    up      = 2
    down    = 3