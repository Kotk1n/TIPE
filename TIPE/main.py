import pygame as pg
from entité import Player
from grille import astar
import random
from transfoimage import transfoimage
from PIL import Image
import random
import numpy as np

fichierimage = "assets/maquettehall1.jpg"
imageSource = Image.open(fichierimage)
nbrpoint=3

pg.init() #lancement pygame
taillecarre = 6
ecranx =720
couleurcase = (100, 100, 100)


pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx + taillecarre, ecranx + taillecarre))
imagefond = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran


def creerrect():
    tempo = []
    while len(tempo)!=2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append(pg.mouse.get_pos())
    rect = pg.Rect(tempo[0][0],tempo[0][1],tempo[1][0]-tempo[0][0],tempo[1][1]-tempo[0][1])
    return(rect)

def creation(n):
    Zonedep=[]
    for i in range(int(n)):
        Zonedep.append(creerrect())
        print(i+1)
    return (Zonedep)

nbrrect = input("Nombre de rect")



#création labi, obstacle
labi =[]
#labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecranx // taillecarre)]
labi = transfoimage(imageSource)


obstacle =[]
coorddepart = []


for i in range(len(labi)):
    for j in range(len(labi)):
        if labi[i][j] == 2:
            coorddepart.append((i, j))
        elif labi[i][j] == 0:
            obstacle.append((i, j))





#création liste point
Point = []
CoordDepArr=[]


def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2





#calcul chemin pour chaque point
path =[]




pressed = True
#lancement fenêtre
running = True

def mouvementauto (M,point):


    if ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x < 0:
        point.rect.x += -1
    elif ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x > 0:
        point.rect.x += 1
    if ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y < 0:
        point.rect.y += -1
    elif ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y > 0:
        point.rect.y += 1
    actualisation()

#boucle principal
defrect = False
while running:

    if defrect==False:
        ecran.blit(imagefond, (0, 0))

        for i in range(len(obstacle)):
            pg.draw.rect(ecran, (0, 0, 0),(obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))

        pg.display.flip()
        Point = []
        Zonedep = creation(nbrrect)
        for i in range(nbrpoint):
            rectdep = random.choice(Zonedep)
            x1 = random.randint(rectdep[0], rectdep[0] + rectdep[2])
            y1 = random.randint(rectdep[1], rectdep[1] + rectdep[3])
            rectar = random.choice(Zonedep)
            while rectar == rectdep:
                rectar = random.choice(Zonedep)
            x2 = random.randint(rectar[0], rectar[0] + rectar[2])
            y2 = random.randint(rectar[1], rectar[1] + rectar[3])
            Point.append(Player(x1, y1, x2, y2,taillecarre))
            pg.draw.rect(ecran, (255, 0, 0), (x1 * taillecarre, y1 * taillecarre, taillecarre, taillecarre))
        path = []

        for i in range(len(Point)):
            carréx = Point[i].centre[0] // taillecarre
            carréy = Point[i].centre[1] // taillecarre
            Point[i].carré = (carréx, carréy)
        for i in range(len(Point)):
            path = path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre), (Point[i].arrivé[0]//taillecarre,Point[i].arrivé[0]//taillecarre))]
            path[i].insert(0, (0, 0))
        defrect = True
    else:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                pressed = True

            if event.type == pg.KEYUP:
                pressed= False

            if pressed:
                ecran.blit(imagefond, (0, 0))
                for i in range(len(obstacle)):
                    pg.draw.rect(ecran, (0, 0, 0),
                                 (obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))

                for i in range(len(Point)):
                    if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                           path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
                        mouvementauto(path[i], Point[i])


                    elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                                  path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
                        if Point[i].compteur + 2 < len(path[i]):
                            Point[i].compteur += 1
                for i in range(len(Point)):
                    ecran.blit(Point[i].image, Point[i].rect)
                pg.display.flip()
    #actualisation visuelle écran
    pg.display.flip()





