import pygame as pg
from game import Game
from entité import Player


game = Game() #importation
pg.init() #lancement pygame

#création liste point
L = []

n=6
for  i in range (n):
    L.append(Player(200+50*i,100))




#Position toutes flèches



fleched =[

    [pg.Rect(200, 80, 200, 200), pg.Rect(180, 80, 150, 100)],

]
flecheg =[
    [pg.Rect(550, 550, 100, 200), pg.Rect(520, 550, 150, 100)],

]
flecheb =[

    [pg.Rect(600, 80, 200, 200), pg.Rect(600, 60, 100, 150)],

]
flecheh =[

    [pg.Rect(200, 400, 200, 200), pg.Rect(200, 370, 100, 150)],

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
        elif game.pressed.get(pg.K_LEFT) and L[i].rect.x > 0 and not((game.mur.rect).collidepoint(L[i].rect.x,L[i].rect.y)):
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






#lancement fenêtre
running = True




#boucle principal
while running:





    #déplacement flèche
    v =2
    for j in range(len(L)):
        for i in range(len(fleched)):
            if fleched[i][1].contains(L[j].rect) and not (L[j].rect.colliderect(game.mur.rect)):

                L[j].rect.x += v

        for i in range(len(flecheg)):
            if flecheg[i][1].contains(L[j].rect) and not (L[j].rect.colliderect(game.mur.rect)):
                L[j].rect.x -= v

        for i in range(len(flecheb)):
            if flecheb[i][1].contains(L[j].rect) and not (L[j].rect.colliderect(game.mur.rect)):
                L[j].rect.y += v

        for i in range(len(flecheh)):
            if flecheh[i][1].contains(L[j].rect) and not (L[j].rect.colliderect(game.mur.rect)):
                L[j].rect.y-= v




    mouvement() #execution déplacement clavier




    screen.blit(background,(0,0))     #affichage du fond blanc



    #affichage de toutes les flèches
    for i in range (len(fleched)):
        pg.draw.rect(screen, (255, 0, 0), fleched[i][1])
        screen.blit(game.fleched.image, fleched[i][0])
    for i in range (len(flecheg)):
        pg.draw.rect(screen, (255, 0, 0), flecheg[i][1])
        screen.blit(game.flecheg.image, flecheg[i][0])
    for i in range (len(flecheb)):
        pg.draw.rect(screen, (255, 0, 0), flecheb[i][1])
        screen.blit(game.flecheb.image, flecheb[i][0])
    for i in range (len(flecheh)):
        pg.draw.rect(screen, (255, 0, 0), flecheh[i][1])
        screen.blit(game.flecheh.image, flecheh[i][0])


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





