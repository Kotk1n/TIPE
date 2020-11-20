import pygame as pg
from game import Game
from entité import Player
from grille import astar
import random

game = Game() #importation
pg.init() #lancement pygame
taillecarre = 20




pg.display.set_caption("Test")
screenx =720
screen = pg.display.set_mode((screenx+taillecarre,screenx+taillecarre))
background = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran





#création labi, obstacle
labi =[]
labi =[[0 for j in range (screenx//taillecarre)]for i in range (screenx//taillecarre)]
quadri = []






#création liste point
L = []
P=[]
n=50
for i in range (n):
    P.append((random.randint(0,screenx),random.randint(0,screenx),random.randint(0,screenx),random.randint(0,screenx)))
for  i in range (n):
    L.append(Player(P[i][3],P[i][2],P[i][0],P[i][1],taillecarre))

def actualisation():
    for i in range(len(L)):
        L[i].centre[0] = L[i].rect.x + L[i].taille/2
        L[i].centre[1] = L[i].rect.y + L[i].taille/2



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


#calcul chemin pour chaque point
path =[]
for i in range(len(L)):
    path =  path + [astar(labi,(L[i].rect.x//taillecarre,L[i].rect.y//taillecarre), L[i].arrivé)]
    path[i].insert(0,(0,0))




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
while running:

    screen.blit(background,(0,0))     #affichage du fond blanc

    for i in range (len(L)):
        carréx = L[i].centre[0]//taillecarre
        carréy = L[i].centre[1]//taillecarre
        L[i].carré = (carréx,carréy)




    print("path",path)


    mouvement() #execution déplacement clavier







    for i in range (screenx//taillecarre+taillecarre):
        if i%2 ==0:

            for j in range (screenx//taillecarre+taillecarre):
                if j%2==0:

                    pg.draw.rect(screen, (255, 255, 255), (i*taillecarre, j*taillecarre, taillecarre, taillecarre))
                else:
                    pg.draw.rect(screen, (0, 255, 255), (i*taillecarre, j*taillecarre, taillecarre, taillecarre))
        else:
            for j in range (screenx//taillecarre+taillecarre):
                if j%2==0:
                    pg.draw.rect(screen, (0, 255, 255), (i*taillecarre, j*taillecarre, taillecarre, taillecarre))

                else:
                    pg.draw.rect(screen, (255, 255, 255), (i*taillecarre, j*taillecarre, taillecarre, taillecarre))
    for i in range (len(L)):
        pg.draw.rect(screen, (0, 255, 0), (L[i].arrivé[0]*taillecarre, L[i].arrivé[1]*taillecarre, taillecarre, taillecarre))





    #affichage points
    for i in range(len(L)):
         screen.blit(L[i].image,L[i].rect)




    for i in range(len(L)):
        if L[i].centre != [path[i][L[i].compteur+1][0]*taillecarre +taillecarre/2,path[i][L[i].compteur+1][1]*taillecarre +taillecarre/2]:
            mouvementauto(path[i],L[i])
            print("centre",L[i].centre)
            print(list((path[i][L[i].compteur+1][0]*taillecarre +taillecarre/2, path[i][L[i].compteur+1][1]*taillecarre +taillecarre/2)))
        elif L[i].centre == list((path[i][L[i].compteur+1][0]*taillecarre +taillecarre/2, path[i][L[i].compteur+1][1]*taillecarre +taillecarre/2)):
            if  L[i].compteur+2 < len(path[i]):
                L[i].compteur +=1




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





