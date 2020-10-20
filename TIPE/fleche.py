import pygame as pg


class flecheg(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.transform.scale(pg.image.load(("assets/flecheg.png")),(100,100))
        self.rect = self.image.get_rect()

class flecheh(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.transform.scale(pg.image.load(("assets/flecheh.png")),(100,100))
        self.rect = self.image.get_rect()

class fleched(pg.sprite.Sprite):

    def __init__(self):
        self.image = pg.transform.scale(pg.image.load(("assets/fleched.png")),(100,100))
        self.rect = self.image.get_rect()

class flecheb(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.transform.scale(pg.image.load(("assets/flecheb.png")),(100,100))
        self.rect = self.image.get_rect()