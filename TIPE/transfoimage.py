from PIL import Image
import numpy as np

""" 

0 c'est noir 1 c'est blanc


 """
fichierimage = "assets/maquettehall1.jpg"
imageSource = Image.open(fichierimage)
taillepixel = 120


def transfoimage(imageSource):
    # on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    Image = imageSource.convert("L")
    (taille, taille) = Image.size
    print("taille de l'image=", Image.size)
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
    return (ImageP)

'''
# Imageshow=pixelisation(imageSource,120)
Imageshow = transfoimage(imageSource)
tailleimageshow = len(Imageshow)
print(len(Imageshow))

img = Image.new('RGB', (tailleimageshow, tailleimageshow), color='white')

for X in range(tailleimageshow):
    for Y in range(tailleimageshow):

        if Imageshow[X][Y] == 0:
            img.putpixel((X, Y), (0, 0, 0, 255))
        elif Imageshow[X][Y] == 1:
            img.putpixel((X, Y), (200, 200, 200, 255))

img.show()
'''