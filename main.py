import pygame as pg
from entité import Player
from grille import astar
from transfoimage import transfoimage
from transfoimage import fichierimage
import random

pressed = True

def creerrect():
    tempo = []
    while len(tempo)!=2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append((pg.mouse.get_pos()))
    rect = pg.Rect(tempo[0][0],tempo[0][1],tempo[1][0]-tempo[0][0],tempo[1][1]-tempo[0][1])
    return(rect)

def creation(n):
    Zonedep=[]
    for i in range(int(n)):
        Zonedep.append(creerrect())
        print(i+1)
    return (Zonedep)

nbrrect = input("Nombre de rect")
#lancement pygame
pg.init()
# choix image fond d'ecran
imagefond = pg.image.load(fichierimage)
#récupère la taille de l'image choisi
(ecranx, ecrany) = imagefond.get_size()
#couleurcase = (100, 100, 100)

pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx, ecrany))



#création labi, obstacle
#labi=[]
#labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecrany // taillecarre)]
#0
labi = transfoimage()


#définition à partir de l'image transformé les points de l'image étant des murs et ceux étant des coordonnées d'entrées/sortie
obstacle = []
coorddepart = []

'''
for i in range(len(labi)):
    for j in range(len(labi)):
        if labi[i][j] == 0:
            obstacle.append((i, j))
        elif labi[j][i] == 2:
            coorddepart.append((i, j))'''
##à vérifier : si la liste donné est propre


#création liste point


'''Point = []

for i in range(nbrpoint):
    x1 = random.choice(coorddepart)
    x2 = x1
    while x2 == x1:
        x2 = random.choice(coorddepart)
    print("départ", "x", x1[0], "y", x1[1], "arrivé x", x2[0], "y", x2[1])
    ecran.blit(pg.image.load("/home/utilisateur/Bureau/TIPE-Test-fusion-/TIPE/assets/violet.png"), (x1[1], x1[0]))
    print(labi[x1[0]][x1[1]])
'''



#calcul chemin pour chaque point

#path[i] est le chemin emprunté par le point n°i

#lancement fenêtre
running = True
#M:Path du point i et point : i


def mouvementauto(pathi, i):
    if Point[i].compteur + 1 < len(path[i]):
        Point[i].rect.x = pathi[Point[i].compteur + 1][0]
        Point[i].rect.y = pathi[Point[i].compteur + 1][1]


ecran.blit(imagefond, (0, 0))     #affichage du fond blanc

defrect=False
#boucle principal
while running:
    if defrect==False:
        ecran.blit(imagefond, (0, 0))
        pg.display.flip()
        nbrpoint = 2
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
            Point.append(Player(x1, y1, x2, y2))
        path = []
        for i in range(len(Point)):
            path = path + [astar(labi, (Point[i].rect.x, Point[i].rect.y), Point[i].arrivé)]
        print("path", path)
        defrect=True
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

                for i in range(len(Point)):

                    mouvementauto(path[i], i)

                    Point[i].compteur += 1

                for i in range(len(Point)):
                    ecran.blit(Point[i].image, Point[i].rect)
                pg.display.flip()
    #actualisation visuelle écran
    pg.display.flip()






