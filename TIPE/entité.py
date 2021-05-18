import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self,x,y,a,b,c):

        self.velocity = 1.5
        self.taille = 10
        self.image = pg.transform.scale(pg.image.load("assets/cercle.png"),(self.taille,self.taille))
        self.imageinf = pg.transform.scale(pg.image.load("assets/cerclerouge.png"),(self.taille,self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.arrivé = (a,b)
        self.compteur = 0
        self.carré = (0,0)
        self.centre = [self.rect.x + self.taille/2,self.rect.y + self.taille/2]
        self.actif = (False,-1,-1)
        self.tempsactivite =[-1,-1]
        self.etat = "sain"
        self.tempsinf = [-1,-1]
        self.pause = [False,-1,-1] #pause[1] = temps de fin de pause


    def move_right (self):
        self.rect.x += self.velocity

    def move_left (self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
    def move_down (self):
        self.rect.y += self.velocity

