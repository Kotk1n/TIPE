from entité import Player
from fleche import *
from mur import mur
class Game:


    def __init__(self):
        self.mur = mur()
        self.fleched = fleched()
        self.flecheg = flecheg()
        self.flecheh = flecheh()
        self.flecheb = flecheb()
        self.pressed = {   #dictionnaire qui va contenir les paires (touches + True si appuyé False si relaché)

        }
