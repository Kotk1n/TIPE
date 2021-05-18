import sqlite3
import random
con = sqlite3.connect('donnees.db')
cur = con.cursor()
""""
def creerbdd():
    cur = con.cursor()
    con.execute(
        "CREATE TABLE evenements (Temps	REAL,particule1	INTEGER,particule2	INTEGER,px	REAL,py	REAL)")

    con.execute(
        "CREATE TABLE temps (Particule	INTEGER,Temps	REAL)")
"""


def remisea0 ():

    cur.execute("delete from evenements")
    cur.execute("delete from temps")

    con.commit()



def enregistrement_contact(t,p1,p2,x,y):
    cur.execute("insert into evenements values ({},{},{},{},{})".format(t,p1,p2,x,y))
    con.commit()
def enregistrement_durée(p,act):
    (tempsdep, tempsar)=act
    tempsact=tempsar-tempsdep
    cur.execute("insert into temps values ({},{})".format(p,tempsact))



def analyse_essai():
    #trouve le nombre de contact ayant était fait au cours de l'essai
    cur.execute("""SELECT count() FROM evenements""")
    nombre_contact=cur.fetchone()[0]
    print(nombre_contact)
    cur.execute("""SELECT avg(Temps) from temps """)
    tempsmoyen=cur.fetchone()[0]
    print(tempsmoyen)
analyse_essai()
nombre_fleche_max=30

###l'idée de l'algorithme

 #on ajoute une flèche, si le compte rendu est meille
 #si le temps est mauvais recommence à zero ?



distancemin=10    #distance(distance avec norme carré) minimal à un mur
def proche_mur(point,labi):
    x=point(0)
    y=point(1)
    for k in range(x-distancemin,x+distancemin):
        for l in range (y-distancemin,y+distancemin):
            if labi[k][l]==0:
                return True
    return False


###vérifier le bon balayage
def ajout_fleche(Lfleches, labi):

    #trouve un point libre de la map
    point=(randint(ecranx),randint(ecranx))
    #vérifie pas trop prêt d'un mur:

    while proche_mur(point,labi):
        point = (randint(ecranx), randint(ecranx))
    fleche=[]

    #version avec diagonale
    orient=randint(1,8)
    (x,y)=point
    #à modifier
    taille_fleche=randint(10,50)
    if orient==1:
        for i in range(taille_fleche):
            fleche.append[(x+i,y)]
    elif orient==2:
        for i in range(taille_fleche):
            fleche.append[(x+i,y+i)]
    elif orient==3:
        for i in range(taille_fleche):
            fleche.append[(x,y+i)]
    elif orient==4:
        for i in range(taille_fleche):
            fleche.append[(x-i,y+i)]
    elif orient==5:
        for i in range(taille_fleche):
            fleche.append[(x-i,y)]
    elif orient==6:
        for i in range(taille_fleche):
            fleche.append[(x-i,y-i)]
    elif orient==7:
        for i in range(taille_fleche):
            fleche.append[(x,y-i)]
    elif orient==8:
        for i in range(taille_fleche):
            fleche.append[(x+i,y-i)]
    Lfleches.append(fleche)
    return Lfleches


#verifie qu'il n'y a pas déjà trop de fleche



