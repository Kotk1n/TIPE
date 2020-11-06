import pygame as pg
from game import Game
from entité import Player
from grille import astar

game = Game() #importation
pg.init() #lancement pygame



labi = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



start = (0, 0)
end = (11, 6)

#création liste point
L = []

n=1
for  i in range (n):
    L.append(Player(00+50*i,00))





#Position toutes flèches



fleched =[

    [pg.Rect(200, 80, 200, 200), pg.Rect(230, 80, 150, 100)],
    [pg.Rect(300, 80, 200, 200), pg.Rect(330, 80, 150, 100)],
    [pg.Rect(400, 80, 200, 200), pg.Rect(430, 80, 150, 100)],
    [pg.Rect(500, 80, 200, 200), pg.Rect(530, 80, 150, 100)],

]
flecheg =[
    [pg.Rect(550, 550, 100, 200), pg.Rect(520, 550, 150, 100)],
    [pg.Rect(450, 550, 100, 200), pg.Rect(420, 550, 150, 100)],
    [pg.Rect(350, 550, 100, 200), pg.Rect(320, 550, 150, 100)],
    [pg.Rect(250, 550, 100, 200), pg.Rect(220, 550, 150, 100)],


]
flecheb =[

    [pg.Rect(600, 80, 200, 200), pg.Rect(600, 60, 100, 150)],
    [pg.Rect(600, 180, 200, 200), pg.Rect(600, 160, 100, 150)],
    [pg.Rect(600, 280, 200, 200), pg.Rect(600, 260, 100, 150)],
    [pg.Rect(600, 380, 200, 200), pg.Rect(600, 360, 100, 150)],
    [pg.Rect(600, 480, 200, 200), pg.Rect(600, 460, 100, 150)]

]
flecheh =[

    [pg.Rect(200, 400, 200, 200), pg.Rect(200, 420, 100, 150)],
    [pg.Rect(200, 500, 200, 200), pg.Rect(200, 520, 100, 150)],
    [pg.Rect(200, 300, 200, 200), pg.Rect(200, 320, 100, 150)],
    [pg.Rect(200, 200, 200, 200), pg.Rect(200, 220, 100, 150)],
    [pg.Rect(200, 100, 200, 200), pg.Rect(200, 120, 100, 150)]
]

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

path = astar(labi,start, end)

compteur=0
M = [(0,0),(11,6)]
def mouvementauto (M,point,compteur):
    point.rect.x += (M[compteur + 1][0]-M[compteur ][0])
    point.rect.y += (M[compteur + 1][1]-M[compteur ][1])

#lancement fenêtre
running = True



#boucle principal
while running:

    for i in range (len(L)):
        carréx = L[i].rect.x//60
        carréy = L[i].rect.y//60
        carré=(carréx,carréy)
        print(carré)
        print("position",L[i].rect.x,L[i].rect.y)


    taillecarre = 60









    mouvement() #execution déplacement clavier




    screen.blit(background,(0,0))     #affichage du fond blanc


    if compteur+1 < len(path):
        if carré != path[compteur+1]:
            mouvementauto(path, L[0], compteur)
        else:
            compteur +=1


    print(carré)




    #affichage points
    for i in range(len(L)):
         screen.blit(L[i].image,L[i].rect)


    # affichage mur
    screen.blit(game.mur.image,game.mur.rect)



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





