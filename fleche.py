import pygame as pg

class flecheg(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.image.load(("assets/flecheg.png"))


class flecheh(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.image.load(("assets/flecheh.png"))


class fleched(pg.sprite.Sprite):

    def __init__(self):
        self.image = pg.image.load("assets/fleched.png")

class flecheb(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.image.load(("assets/flecheb.png"))
