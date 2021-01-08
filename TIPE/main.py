import pygame as pg
from entité import Player
from grille import astar
from transfoimage import transfoimage
import random



pg.init() #lancement pygame
taillecarre = 1
ecranx =720
ecrany = 720
couleurcase = (100, 100, 100)


pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx + taillecarre, ecrany + taillecarre))
imagefond = pg.image.load("assets/hallcarré.jpg") # choix image fond d'ecran





#création labi, obstacle
labi =[]
#labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecrany // taillecarre)]
labi = transfoimage()





nbrcasedepart=20

obstacle =[]
coorddepart = []

nbrobstacle = 50


for i in range (len(labi)):
    for j in range (len(labi)):
        if labi[i][j] ==1:
            obstacle.append((i,j))
        if labi[i][j] ==2:
            coorddepart.append((i,j))
print(type(coorddepart))
Zonedep=[]
testlist = coorddepart

print(testlist)
while len(testlist) > 0:
    testpoint = testlist[0]
    pointproxi = testpoint
    while pointproxi in coorddepart:
        pointproxi = (pointproxi[0]-1,pointproxi[1])
    pointproxi = (pointproxi[0]+1,pointproxi[1])
    while pointproxi in coorddepart:
        pointproxi = (pointproxi[0],pointproxi[1]-1)
    coingauche = (pointproxi[0],pointproxi[1]+1)
    pointproxi = testpoint
    while pointproxi in coorddepart:
        pointproxi = (pointproxi[0] + 1, pointproxi[1])
    pointproxi = (pointproxi[0] - 1, pointproxi[1])
    while pointproxi in coorddepart:
        pointproxi = (pointproxi[0], pointproxi[1] + 1)
    coindroit = (pointproxi[0], pointproxi[1] - 1)
    Zonedep = Zonedep + [pg.rect(coingauche[0],coingauche[1],coindroit[0]-coingauche[0],coindroit[1]-coingauche[1])]
    for i in testlist:
        if i in Zonedep:
            testlist.remove(i)

print(Zonedep)





#création liste point
'''Point = []
CoordDepArr=[]
nbrpoint=50
for i in range (nbrpoint):
    x1 = random.choice(coorddepart)
    x2 = x1
    while x2 == x1:
        x2 = random.choice(coorddepart)

    CoordDepArr.append((x1[0],x1[1],x2[0],x2[1]))

for  i in range (nbrpoint):
    Point.append(Player(CoordDepArr[i][0] , CoordDepArr[i][1], CoordDepArr[i][2], CoordDepArr[i][3], taillecarre))

def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2





#calcul chemin pour chaque point
path =[]
for i in range(len(Point)):

    path =  path + [astar(labi, (Point[i].rect.x, Point[i].rect.y), Point[i].arrivé)]

    print("path",path)

path = []
for i in range(nbrpoint):
    path += [[(120,400),(600,200),(320,100),(40,600)]]
print(path)


def mouvementauto (M,point):

    pas = 10
    if ((M[point.compteur+1][0]*taillecarre + taillecarre) - point.taille )- point.rect.x < 0:
        point.rect.x += -pas
    elif ((M[point.compteur+1][0]*taillecarre + taillecarre) - point.taille )- point.rect.x > 0:
        point.rect.x += pas
    if ((M[point.compteur+1][1]*taillecarre + taillecarre) - point.taille )- point.rect.y < 0:
        point.rect.y += -pas
    elif ((M[point.compteur+1][1]*taillecarre + taillecarre) - point.taille )- point.rect.y > 0:
        point.rect.y += pas
    actualisation()

#lancement fenêtre
running = True


#boucle principal
while running:
    ecran.blit(imagefond, (0, 0))  # affichage du fond blanc
    for j in range(len(labi)):
        for i in range(len(labi[j])):
            if labi[i][j] == 2:
                pg.draw.rect(ecran, (55, 55, 55), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))
            if labi[i][j] == 0:
                pg.draw.rect(ecran, (55, 0, 55), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))

    for i in range (len(Point)):
        carréx = Point[i].centre[0] // taillecarre
        carréy = Point[i].centre[1] // taillecarre
        Point[i].carré = (carréx, carréy)




    for i in range(len(Point)):
        if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
            mouvementauto(path[i], Point[i])


        elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
            if  Point[i].compteur+2 < len(path[i]):
                Point[i].compteur +=1




    #affichage points
    for i in range(len(Point)):
         ecran.blit(Point[i].image, Point[i].rect)

    #actualisation visuelle écran
    pg.display.flip()




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()'''
