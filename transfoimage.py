from PIL import Image
fichierimage="TIPE/assets/hallcarré2.jpg"
def transfoimage():
    global width,height,petit
    imageSource=Image.open(fichierimage)

    #on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    image2=imageSource.convert("L")

    (height, width)=image2.size
    print("taille de l'image=",image2.size)
    petitL=[]
    grandL=[]
    for x in range(height):
        for y in range (width):


            if image2.getpixel((x,y)) > 50:
                petitL+=[1]
            else:
                petitL+=[0]

        grandL.append(petitL)
        petitL=[]

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
            img.putpixel((j, i), (255, 0, 0, 255))


img.show()
'''