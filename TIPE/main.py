import pygame as pg
from game import Game
from entité import Player
from grille import astar
import random

game = Game() #importation
pg.init() #lancement pygame



labi = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



start = (0, 0)
end = (11, 6)
Ma=[(200,256),(475,547),(532,348),(102,521)]
#création liste point
L = []
P=[]
n=4
for i in range (n):
    P.append((random.randint(0,600),random.randint(0,600)))
for  i in range (n):
    L.append(Player(0,0,Ma[i][0],Ma[i][1]))


#création écran
pg.display.set_caption("Test")
screen = pg.display.set_mode((720,720))


background = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran



# fonction mouvement clavier + collision mur et écran
def mouvement ():
    for i in range(len(L)):
        x = L[i].rect.x
        y = L[i].rect.y
        if game.pressed.get(pg.K_RIGHT) and L[i].rect.x + L[i].rect.width < screen.get_width() :
            L[i].move_right()
            if L[i].rect.colliderect(game.mur.rect):
                L[i].rect.x = x
                L[i].rect.y = y
        elif game.pressed.get(pg.K_LEFT) and L[i].rect.x > 0:
            L[i].move_left()
            if L[i].rect.colliderect(game.mur.rect):
                L[i].rect.x = x
                L[i].rect.y = y
        elif game.pressed.get(pg.K_UP) and L[i].rect.y > 0:
            L[i].move_up()
            if L[i].rect.colliderect(game.mur.rect):
                L[i].rect.x = x
                L[i].rect.y = y
        elif game.pressed.get(pg.K_DOWN) and L[i].rect.y + L[i].rect.height < screen.get_height():
            L[i].move_down()
            if L[i].rect.colliderect(game.mur.rect):
                L[i].rect.x = x
                L[i].rect.y = y
path =[]
for i in range(len(L)):
    path =  path + [astar(labi,(L[i].rect.x//60,L[i].rect.y//60), L[i].arrivé)]

compteur=0

print("path",path)
#lancement fenêtre
running = True

def mouvementauto (M,point,compteur):

    point.rect.x += (M[compteur + 1][0]-M[compteur][0])
    point.rect.y += (M[compteur + 1][1]-M[compteur][1])

print (path[1])
#boucle principal
while running:

    for i in range (len(L)):
        carréx = L[i].rect.x//60
        carréy = L[i].rect.y//60
        carré=(carréx,carréy)

    taillecarre = 60





    mouvement() #execution déplacement clavier




    screen.blit(background,(0,0))     #affichage du fond blanc




    #affichage points
    for i in range(len(L)):
         screen.blit(L[i].image,L[i].rect)


    # affichage mur
    screen.blit(game.mur.image,game.mur.rect)

    for i in range(len(L)):


        if compteur + 1 < len(path[i]):
            if i==1:
                print("carré", i, carré)
                print("path1",path[1][compteur+1])
                print("position", i, L[i].rect.x, L[i].rect.y)
                print("arrivé", i, L[i].arrivé)
            if carré != path[i][compteur + 1]:
                mouvementauto(path[i], L[i], compteur)
            else:
                compteur += 1




    #actualisation visuelle écran
    pg.display.flip()



    #détection entrée clavier
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif  event.type == pg.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False





