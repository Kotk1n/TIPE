from PIL import Image
import numpy as np
import pygame as pg

""" 

0 c'est noir 1 c'est blanc


 """
fichierimage = "assets/hallcarré.png"
imageSource = Image.open(fichierimage)
taillepixel = 120


def transfoimage(imageSource):
    # on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    Image = imageSource.convert("L")
    (taille, taille) = Image.size

    MatriceImage = np.zeros((taille, taille))
    for X in range(taille):
        for Y in range(taille):
            # si c'est blanc
            if Image.getpixel((X, Y)) > 50:
                MatriceImage[X,Y] = 1
            # si c'est noir
            else:
                MatriceImage[X,Y] = 0


    return (MatriceImage)
#fonction qui à partir de la matrice representant la carte renvoi une image avec les dimensions voulu.
def creation_image(tailleimage,taillepixel,ImageP):
    img = Image.new('RGB', (tailleimage, tailleimage), color='white')
    for X in range(n):
        for Y in range(n):
            for k in range(taillepixel):
                for l in range(taillepixel):
                    if ImageP[X][Y] == 0:
                        img.putpixel((k + X * taillepixel, l + Y * taillepixel), (0, 0, 0, 255))


                    elif ImageP[X][Y] == 1:
                        img.putpixel((k + X * taillepixel, l + Y * taillepixel), (250, 250, 250, 255))
    img = img.save("imagepixel.png")

def pixelisation(image, n):
    # image, et taille des nouveaux "pixels" attention , n doit être un multiple de la taille de l'image.
    ImageP = np.zeros((n, n))

    # on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    image = image.convert("L")
    # on récupère la taille de l'image
    (taille, taille) = image.size
    tailleimage = int(taille)
    taillepixel = tailleimage // n

    for X in range(n):
        for Y in range(n):
            # calcul de la moyenne du bloc
            s = 0
            for k in range(taillepixel):
                for l in range(taillepixel):
                    s += image.getpixel((k + X * taillepixel, l + Y * taillepixel))
            s = s / (taillepixel ** 2)
            if s > 128:
                ImageP[X][Y] = 1
            else:
                ImageP[X][Y] = 0
    #pour éviter les diagonales
    for X in range(1,n-1):
        for Y in range(1,n-1):
            if ImageP[X][Y]==0:
                if ImageP[X + 1][Y - 1] == 0 or ImageP[X - 1][Y - 1] == 0:
                    ImageP[X][Y-1]=0



    return (ImageP)


#fonction qui à partir d'une image pixellisé en 1 matrice renvoi la matrice avec les corrections voulant être apportés manuellement (obstacle,terraforming)
def correction(ImageP):
    image = pg.image.load("imagepixel.png")
    running=True
    gauche=1
    droit=3
    ecran = pg.display.set_mode((720,720))
    while running:
        ecran.blit(image, (0, 0))
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                clic=event.button
                pos=pg.mouse.get_pos()
                if event.button==gauche:
                    ImageP[pos[0]//6][pos[1]//6]=1
                if event.button==droit:
                    ImageP[pos[0]//6][pos[1]//6]=0
            if event.type == pg.QUIT:
                running = False
    pg.quit()
    return(ImageP)






'''
lienimage="assets/hallcarré.png"
(Imageshow)=pixelisation(imageSource,120)
#Imageshow = transfoimage(imageSource)
Imageshow=Image.open("imagepixel.png")
Imageshow.show()
'''

