import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self,x,y,a,b):

        self.velocity = 1.5
        self.taille = 10
        self.image = pg.transform.scale(pg.image.load("bleu.png"),(self.taille,self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.arrivé = (a,b)
        self.compteur = 0





    def move_right (self):
        self.rect.x += self.velocity

    def move_left (self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
    def move_down (self):
        self.rect.y += self.velocity

