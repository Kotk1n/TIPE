from PIL import Image
def transfoimage():
    global longueur,largeur,petit
    imageSource=Image.open("assets/maquettehall2.jpg")
    #on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    image2=imageSource.convert("L")
    (longueur,largeur)=image2.size
    petitL=[]
    grandL=[]
    for y in range (largeur):
        for x in range (longueur):

            if image2.getpixel((x,y)) > 200:
                petitL+=[1]
            elif image2.getpixel((x,y)) < 100 :
                petitL+=[0]
            else :
                petitL +=  [2]
        grandL.append(petitL)
        petitL=[]

    return(grandL)

transfoimage()

