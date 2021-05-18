import pygame as pg
from entité import Player
from grille import astar
import random
from transfoimage import transfoimage, pixelisation
from PIL import Image
import random
import numpy as np

"""
from bdd import enregistrement_contact,enregistrement_durée,analyse_essai
from bdd import remisea0
"""
import sqlite3

# import de la "carte"
fichierimage = "assets/hallcarré.png"
# transformation de l'image au format de PIL
imageSource = Image.open(fichierimage)
# renvoi un tableau representant la carte avec 1 si la case est libre et 0 si la case est un obstacle
labi = pixelisation(imageSource, 120)

# transformation de l'image au format de pygame
image = pg.image.load(fichierimage)
imagep = pg.image.load("imagepixel.png")

# nombre d'individus simulés
nbrpoint = 100
# la distance à laquelle deux individus risque une infection
distancesecu = 30
# la fréquence d'apparition d'individu
frequence = 50

pg.init()  # lancement pygame
# la taille du carré qui représente un individu
taillecarre = 6
# on choisira une image en 720*720
ecranx = 720
couleurcase = (100, 100, 100)

# donne le nom de la fenétre
pg.display.set_caption("Simulation épidémiologique")

# renvoi la dimension de l'écran
ecran = pg.display.set_mode((ecranx + taillecarre, ecranx + taillecarre))

# choix image fond d'ecran
'''imagefond = pg.image.load("assets/blanc.jpg") '''

Pointactif = []
listeposcontact = []


# fonction qui créer des rectangles pygame à partir des cliques de la souris
def creerrect():
    tempo = []
    while len(tempo) != 2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append(pg.mouse.get_pos())
    rect = pg.Rect(tempo[0][0], tempo[0][1], tempo[1][0] - tempo[0][0], tempo[1][1] - tempo[0][1])
    return (rect)


# (possible que c'est rect soit fait automatiquement à l'aide d'un code couleur pour l'image )
def prendposition():
    tempo = []
    while len(tempo) != 1:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                tempo.append(pg.mouse.get_pos())
    return (tempo)


# fonction qui créer les n zones de départs duquel les individus proviennent.
def creation_porte(n):
    Zonedep = []
    for i in range(int(n)):
        Zonedep.append(creerrect())
        print("la zone de départ", i + 1, "a été créer")
    return (Zonedep)


def creation_fleche(nbrefleche):
    zonefleches = []
    for k in range(int(nbrefleche)):
        print("veuillez cliquer sur le sommet haut-gauche puis bas droit de la flèche voulant être créé")
        # récolte la position du clic au format de la fenêtre
        clic1 = prendposition()[0]
        # transforme la position du clic au format de l'image "pixellisé"
        point1 = [clic1[0] // 6, clic1[1] // 6]
        clic2 = prendposition()[0]
        point2 = [clic2[0] // 6, clic2[1] // 6]
        fleche = []
        for x in range(int(point1[0]), int(point2[0])):
            for y in range(int(point1[1]), int(point2[1])):
                fleche.append((x, y))
        print("la fleche", k + 1, "a été créer")
        print(
            "Veuillez indiquer la direction de la zone fléchées(nord,nord-est,est,sud-est,sud,sud-ouest,ouest,nord-ouest")
        direction = str(input())
        zonefleches.append([fleche, direction])
    return (zonefleches)


def regroupement(i, j):
    p = 0.8
    result = random.random()
    if result < p:
        tempspause = random.randint(4, 40) * frequence
        Point[i].pause = (True, compteur + tempspause)
        Point[j].pause = (True, compteur + tempspause)


def testpause():
    for i in range(len(Point)):
        if compteur == Point[i].pause[1]:
            Point[i].pause[0] = False
            actif.append(i)


nbrrect = input("Veuillez indiquer le nombre de zones de départs à créer")
"""
#réinitialise la base de données SQL

remisea0()
"""

obstacle = []
coorddepart = []

# détection des obstables (murs et zones impratiquable) provenant de labi créer au dessus.
for i in range(len(labi)):
    for j in range(len(labi)):
        if labi[i][j] == 0:
            obstacle.append((i, j))

nbrfleche = input("Veuillez indiquer le nombre de fléches à créer")

# initialise le compteur , qui sera l'indicateur du "temps" dans notre simulation
compteur = 0
# création de la liste des point et de leurs coordonnées d'arrivées respectives.
Point = []
CoordDepArr = []


# alerte covid est la fonction qui renvoi si deux individus sont trop proche signifiant un contact dangereux.
def alertecovid(x1, y1, x2, y2):
    global distancesecu, taillecarre
    contact = False
    if np.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) < ((taillecarre) + distancesecu):
        contact = True
    return (contact)


# créer la matrice qui representera les intéractions entre les points . 1 si il y a eux intéraction et 0 sinon.
matricecontact = np.zeros((nbrpoint, nbrpoint))


# fonction qui actualise la position des individus sur la representation pygame.
def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2
    print(actif)
    for i in range(len(actif)):
        # cette notation permet d'obtenir la matrice de contact telle que l'on ne calcule pas deux fois la même distance et test entre pts différents
        for j in range(i + 1, len(actif)):
            x1 = Point[actif[i]].rect.x
            y1 = Point[actif[i]].rect.y
            x2 = Point[actif[j]].rect.x
            y2 = Point[actif[j]].rect.y
            if alertecovid(x1, y1, x2, y2):
                if matricecontact[i, j] == 0:
                    listeposcontact.append([(x1 + x2) / 2, (y1 + y2) / 2])
                    """
                    enregistrement_contact(compteur,i,j,(x1+x2)/2,(y1+y2)/2)
                    """
                matricecontact[i, j] = 1
                matricecontact[j, i] = 1
                if Point[actif[i]].infecte or Point[actif[j]].infecte:
                    Point[actif[i]].infecte = True
                    Point[actif[j]].infecte = True
            regroupement(actif[i], actif[j])


pressed = True

# lancement fenêtre
running = True


# fonction permettant le mouvement de chaque point
def mouvementauto(M, point):
    pas = 1

    if ((M[point.compteur + 1][0] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.x < 0:
        point.rect.x += -pas
    elif ((M[point.compteur + 1][0] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.x > 0:
        point.rect.x += pas
    if ((M[point.compteur + 1][1] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.y < 0:
        point.rect.y += -pas
    elif ((M[point.compteur + 1][1] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.y > 0:
        point.rect.y += pas
    actualisation()


# boucle principal
defrect = False
defleche = False
defchemin = False
while running:

    if defrect == False:
        # partie calcul
        ecran.blit(image, (0, 0))  # affichage image blanche fond
        """
        for i in range(len(obstacle)):
            pg.draw.rect(ecran, (0, 0, 0),(obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre)) # affichage obstacle
        """
        pg.display.flip()  # actualisation écran
        Point = []
        Zonedep = creation_porte(nbrrect)  # création des rect
        defrect = True
    # créer les zones fléchées sous formes de blocs rectangulaires auquels leurs sont associées une direction.
    if defleche == False:
        if nbrfleche == 0:
            defleche = True
        else:
            zonefleches = creation_fleche(nbrfleche)
            pg.display.flip()  # actualisation écran
            print(zonefleches)
            defleche = True
    if defchemin == False:
        # choix des coordonnées de depart et d'arrivées de chaque points parmi les rects
        for i in range(nbrpoint):
            rectdep = random.choice(Zonedep)
            x1 = random.randint(rectdep[0], rectdep[0] + rectdep[2])
            y1 = random.randint(rectdep[1], rectdep[1] + rectdep[3])
            rectar = random.choice(Zonedep)
            while rectar == rectdep:
                rectar = random.choice(Zonedep)
            x2 = random.randint(rectar[0], rectar[0] + rectar[2])
            y2 = random.randint(rectar[1], rectar[1] + rectar[3])
            Point.append(Player(x1, y1, x2, y2, taillecarre))

        pointfait = 0
        pointtot = len(Point)
        path = []
        # définition du centre des points et on leur associe à tous un path grâce au A*
        for i in range(len(Point)):
            carréx = Point[i].centre[0] // taillecarre
            carréy = Point[i].centre[1] // taillecarre
            Point[i].carré = (carréx, carréy)
            print("les coordonnées de départ du point", i + 1, "sont",
                  (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre),
                  "et les coordonnées du point d'arrivée sont",
                  (Point[i].arrivé[0] // taillecarre, Point[i].arrivé[1] // taillecarre))
            path = path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre),
                                 (Point[i].arrivé[0] // taillecarre, Point[i].arrivé[1] // taillecarre), pointfait,
                                 pointtot, zonefleches)]
            pointfait += 1
        # établi que la première personne est infécted
        Point[0].actif = True
        Point[0].infecte = True




    else:
        # partie affichage

        ecran.blit(image, (0, 0))

        for i in range(len(Zonedep)):  # affichage Zone de départ
            pg.draw.rect(ecran, (255, 255, 0), Zonedep[i])
        """
        for i in range(len(obstacle)):                                                       #affichage obstacle
            pg.draw.rect(ecran, (0, 0, 0),
                         (obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))
        """
        for i in range(len(path)):  # affichage du chemin
            for j in range(len(path[i])):
                pg.draw.circle(ecran, (255, 0, 255), (path[i][j][0] * taillecarre, path[i][j][1] * taillecarre), 2)

        actif = []
        for i in range(len(Point)):
            if Point[i].actif == True:
                actif.append(i)

        pointaretirer = []
        for i in actif:  # mouvement des points
            if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                   path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
                mouvementauto(path[i], Point[i])

            elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                          path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
                if Point[i].compteur + 2 < len(path[i]):
                    Point[i].compteur += 1
            if Point[i].centre == [path[i][-1][0] * taillecarre + taillecarre / 2,
                                   path[i][-1][1] * taillecarre + taillecarre / 2]:
                pointaretirer.append(i)
            if Point[i].infecte:
                ecran.blit(Point[i].imageinf, Point[i].rect)
            else:
                ecran.blit(Point[i].image, Point[i].rect)
        pg.display.flip()

        compteur = compteur + 1
        testpause()

        if compteur % frequence == 0 and compteur // frequence < len(Point):
            Point[compteur // frequence].actif = True
            Point[compteur // frequence].tempsactivite[0] = compteur
        for i in pointaretirer:
            Point[i].actif = False
            Point[i].tempsactivite[1] = compteur
        for i in actif:
            if Point[i].pause[0] == True:
                actif.remove(i)

            """
            enregistrement_durée(i,Point[i].tempsactivite)
            """

        for event in pg.event.get():  # détection touche
            if event.type == pg.QUIT:
                running = False
                print(matricecontact)
                print("les coordonnées des points où il y a eu des contacts sont", listeposcontact)
                """
                analyse_essai()
                """
                pg.quit()






