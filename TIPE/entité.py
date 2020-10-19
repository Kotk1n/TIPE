import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self,x,y):

        self.velocity = 5
        self.image = pg.image.load("assets/cercle.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def move_right (self):
        self.rect.x += self.velocity

    def move_left (self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
    def move_down (self):
        self.rect.y += self.velocity

