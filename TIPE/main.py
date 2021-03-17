import pygame as pg
from entité import Player
from grille import astar
import random
from transfoimage import transfoimage,pixelisation
from PIL import Image
import random
import numpy as np
from bdd import enregistrement
from bdd import remisea0
import sqlite3


fichierimage = "assets/hallcarré.png"
imageSource = Image.open(fichierimage)
(image,labi)=pixelisation(imageSource,120)


image=pg.image.load("imagepixel.png")

nbrpoint=5
frequence = 20
pg.init() #lancement pygame
taillecarre = 6
ecranx =720
couleurcase = (100, 100, 100)
distancesecu=100

pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx + taillecarre, ecranx + taillecarre))
#imagefond = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran
Pointactif =[]
listeposcontact=[]
#fonction créer rectangle à partir clique souris
def creerrect():
    tempo = []
    while len(tempo)!=2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append(pg.mouse.get_pos())
    rect = pg.Rect(tempo[0][0],tempo[0][1],tempo[1][0]-tempo[0][0],tempo[1][1]-tempo[0][1])
    return(rect)

#regroupement des zones
def creation(n):
    Zonedep=[]
    for i in range(int(n)):
        Zonedep.append(creerrect())
        print(i+1)
    return (Zonedep)





nbrrect = input("Nombre de rect")


"""
#création labi, obstacle
labi =[]
#labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecranx // taillecarre)]
labi = pixelisation(imagePixelisé)
"""
remisea0()

obstacle =[]
coorddepart = []

#détection obstable labi
for i in range(len(labi)):
    for j in range(len(labi)):
        if labi[i][j] == 0:
            obstacle.append((i, j))




compteur =0
#création liste point
Point = []
CoordDepArr=[]

def alertecovid(x1,y1,x2,y2):
    global distancesecu,taillecarre
    contact=False
    if np.sqrt(((x1-x2)**2)+((y1-y2)**2))<(taillecarre)+distancesecu:
        contact=True
    return (contact)

matricecontact=np.zeros((nbrpoint,nbrpoint))


#actualiser position points
def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2
    for i in range (len(actif)):
    # cette notation permet d'obtenir la matrice de contact telle que l'on ne calcule pas deux fois la même distance et test entre pts différents
           for j in range(i + 1, len(actif)):
                x1 = Point[actif[i]].rect.x
                y1 = Point[actif[i]].rect.y
                x2 = Point[actif[j]].rect.x
                y2 = Point[actif[j]].rect.y
                if alertecovid(x1, y1, x2, y2):
                    if matricecontact[i,j]==0:
                        listeposcontact.append([(x1+x2)/2,(y1+y2)/2])
                        enregistrement(compteur,i,j,(x1+x2)/2,(y1+y2)/2)
                    matricecontact[i, j] = 1
                    matricecontact[j, i] = 1

    








pressed = True
#lancement fenêtre
running = True
#fonction permettant le pouvement de chaque point
def mouvementauto (M,point):
    pas = 1

    if ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x < 0:
        point.rect.x += -pas
    elif ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x > 0:
        point.rect.x += pas
    if ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y < 0:
        point.rect.y += -pas
    elif ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y > 0:
        point.rect.y += pas
    actualisation()




#boucle principal
defrect = False
while running:

    if defrect==False:
    #partie calcul
        ecran.blit(image, (0, 0))   #  affichage image blanche fond

        for i in range(len(obstacle)):
            pg.draw.rect(ecran, (0, 0, 0),(obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre)) # affichage obstacle

        pg.display.flip() #actualisation écran
        Point = []
        Zonedep = creation(nbrrect) #création des rect


        #choix des coordonnées de dep et arr parmi les rects
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

        path = []
        # définition du centre des points et on leur associe à tous un path grâce au A*
        for i in range(len(Point)):
            carréx = Point[i].centre[0] // taillecarre
            carréy = Point[i].centre[1] // taillecarre
            Point[i].carré = (carréx, carréy)
            path = path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre), (Point[i].arrivé[0]//taillecarre,Point[i].arrivé[1]//taillecarre))]

        Point[0].actif = True


        defrect = True
    else:
    #partie affichage

        ecran.blit(image, (0, 0))

        for i in range(len(Zonedep)):                                                          #affichage Zone de départ
            pg.draw.rect(ecran,(255,255,0),Zonedep[i])
        """
        for i in range(len(obstacle)):                                                       #affichage obstacle
            pg.draw.rect(ecran, (0, 0, 0),
                         (obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))

        for i in range (len(path)):                                                                   #affichage du chemin
            for j in range(len(path[i])):
                pg.draw.circle(ecran, (255, 0, 255), (path[i][j][0] * taillecarre, path[i][j][1] * taillecarre), 2)
        """
        actif=[]
        for i in range(len(Point)):
            if Point[i].actif ==True:
                actif.append(i)

        aretirer=[]
        for i in actif:                                                                 #mouvement des points
            if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
                mouvementauto(path[i], Point[i])

            elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
                if Point[i].compteur + 2 < len(path[i]):
                    Point[i].compteur += 1
            if Point[i].centre == [path[i][-1][0] * taillecarre + taillecarre / 2,path[i][-1][1] * taillecarre + taillecarre / 2]:
                aretirer.append(i)

            ecran.blit(Point[i].image, Point[i].rect)
        pg.display.flip()



        compteur = compteur + 1

        if compteur%frequence==0 and compteur//frequence<len(Point) :
            Point[compteur//frequence].actif= True
            Point[compteur // frequence].tempsactivite[0]=compteur
        for i in aretirer:
            Point[i].actif = False
            Point[i].tempsactivite[1]=compteur



        for event in pg.event.get():  #détection touche
            if event.type == pg.QUIT:
                running = False
                print(matricecontact)
                print(listeposcontact)
                pg.quit()






