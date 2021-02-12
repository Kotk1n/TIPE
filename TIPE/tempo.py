def creerrect():
    tempo = []
    while len(tempo)!=2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append((pg.mouse.get_pos()))
    rect = pg.Rect(tempo[0][0],tempo[0][1],tempo[1][0]-tempo[0][0],tempo[1][1]-tempo[0][1])
    return(rect)

def creation(n):
    Zonedep=[]
    for i in range(int(n)):
        Zonedep.append(creerrect())
        print(i+1)
    return (Zonedep)

nbrrect = input("Nombre de rect")

defrect=False
#boucle principal
while running:
    if defrect==False:
        ecran.blit(imagefond, (0, 0))
        pg.display.flip()
        nbrpoint = 20
        Point = []
        Zonedep = creation(nbrrect)
        for i in range(nbrpoint):
            rectdep = random.choice(Zonedep)
            x1 = random.randint(rectdep[0], rectdep[0] + rectdep[2])
            y1 = random.randint(rectdep[1], rectdep[1] + rectdep[3])
            rectar = random.choice(Zonedep)
            while rectar == rectdep:
                rectar = random.choice(Zonedep)
            x2 = random.randint(rectar[0], rectar[0] + rectar[2])
            y2 = random.randint(rectar[1], rectar[1] + rectar[3])
            Point.append(Player(x1, y1, x2, y2))
        path = []
        for i in range(len(Point)):
            path = path + [astar(labi, (Point[i].rect.x, Point[i].rect.y), Point[i].arrivé)]
        print("path", path)
        defrect=True
    else:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                pressed = True

            if event.type == pg.KEYUP:
                pressed= False

            if pressed:
                ecran.blit(imagefond, (0, 0))

                for i in range(len(Point)):

                    mouvementauto(path[i], i)

                    Point[i].compteur += 1

                for i in range(len(Point)):
                    ecran.blit(Point[i].image, Point[i].rect)
                pg.display.flip()
    #actualisation visuelle écran
    pg.display.flip()






