from PIL import Image
def transfoimage():
    global width,height,petit
    imageSource=Image.open("assets/hallcarré.jpg")
    #on prend l'image est on la convertie dans un système de couleur 8 bits adapté à pillow
    image2=imageSource.convert("L")
    (height, width)=image2.size
    print(image2.size)
    petitL=[]
    grandL=[]
    for y in range (width):
        for x in range (height):

            if image2.getpixel((x,y)) > 200:
                petitL+=[1]
            elif image2.getpixel((x,y)) < 100 :
                petitL+=[0]
            else :
                petitL +=  [2]
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
        print(i,j)
        if grandL[i][j]==0:
            img.putpixel((j,i),(0,0,0,255))
        elif grandL[i][j]==2:
            img.putpixel((j, i), (0, 200, 0, 255))



img.show()
'''