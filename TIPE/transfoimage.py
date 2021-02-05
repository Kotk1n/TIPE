from PIL import Image
fichierimage="assets/maquettehall1.jpg"
def transfoimage():
    global width,height,petit
    imageSource=Image.open(fichierimage)

    #on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    image2=imageSource.convert("L")

    (height, width)=image2.size
    print("taille de l'image=",image2.size)
    petitL=[]
    grandL=[]
    for x in range (width):
        for y    in range (height):

            if image2.getpixel((x,y)) > 200:
                petitL+=[1]
            elif image2.getpixel((x,y)) < 50:
                petitL += [0]
            else:
                petitL+=[2]

        grandL.append(petitL)
        petitL=[]
    print(grandL)
    return(grandL)


'''
grandL=transfoimage()
print(len(grandL))
print(height, width)
img = Image.new('RGB', (height, width), color='white')

for i in range(width):
    for j in range (height):

        if grandL[i][j]==0:
            img.putpixel((j,i),(0,0,0,255))
        elif grandL[i][j]==1:
            img.putpixel((j, i), (255,0, 0, 255))


img.show()
'''