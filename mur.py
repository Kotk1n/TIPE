import pygame as pg

class mur(pg.sprite.Sprite):

    def __init__(self):
        self.image = pg.image.load("assets/mur.jpg")
        self.rect = self.image.get_rect()
        self.rect.x =400
        self.rect.y = 200



