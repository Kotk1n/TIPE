from math import *
import time
import sqlite3
from transfoimage import transfoimage, pixelisation
from PIL import Image

fichierimage = "assets/hallcarré.png"
imageSource = Image.open(fichierimage)
labi = pixelisation(imageSource, 120)
con = sqlite3.connect('test2.db')
cur = con.cursor()


def remisea0():
    cur.execute("delete from astar2")
    con.commit()


remisea0()


def enregistrement(version2, duree, w):
    cur.execute("insert into astar2 values (?,?,?,?)", (version2, duree, w,essai))
    con.commit()


class Case():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(labi, debut, fin, pointfait, pointot, version, w,essai):
    # créer début fin
    depart = Case(None, debut)
    depart.g = depart.h = depart.f = 0
    arrivee = Case(None, fin)
    arrivee.g = arrivee.h = arrivee.f = 0

    # Initialiser liste
    open_list = []
    closed_list = []

    # rajoute départ à liste ouverte
    open_list.append(depart)

    # Boucle jusque case d'arrivée
    while len(open_list) > 0:

        caseactuelle = open_list[0]
        current_numero = 0
        for numero, case in enumerate(open_list):
            if case.f < caseactuelle.f:
                caseactuelle = case
                current_numero = numero

        # Rajoute la case traitée à la closed liste
        open_list.pop(current_numero)
        closed_list.append(caseactuelle)

        # Vérifie arrivée
        if caseactuelle == arrivee:
            chemin = []
            current = caseactuelle
            while current is not None:
                chemin.append(current.position)  # remonte la liste des cases parcourues
                current = current.parent
            return chemin[::-1]  # retourne la liste

        # génère enfant
        enfant = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:  # cases à coté ,

            case_pos = (caseactuelle.position[0] + new_position[0], caseactuelle.position[1] + new_position[1])

            # Vérification bien dans labi
            if case_pos[0] > (len(labi) - 1) or case_pos[0] < 0 or case_pos[1] > (len(labi[len(labi) - 1]) - 1) or \
                    case_pos[1] < 0:
                continue

            # Vérifie que pas un obstacle
            if labi[case_pos[0]][case_pos[1]] == 0:
                print("recherche du chemin", pointfait, "sur", pointot, "version", version, "w", w,"essai",essai)
                continue

            # crée nouveau noeud
            new_case = Case(caseactuelle, case_pos)

            # ajoute à enfant
            enfant.append(new_case)

        # Loop through enfant
        for i in enfant:

            # Vérifie que noeud pas déjà traité
            for j in closed_list:
                if i == j:
                    continue

            # calcul h ,f ,g
            i.g = caseactuelle.g + 1
            i.h = ((i.position[0] - arrivee.position[0]) ** 2) + ((i.position[1] - arrivee.position[1]) ** 2)

            if version == "XDP":
                i.f = (1 / 2 * w) * (i.g + (2 * w - 1) * i.h + sqrt((i.g - i.h) * 2 + 4 * w * i.g * i.h))
            elif version == "XUP":
                i.f = (1 / 2 * w) * (i.g + i.h + sqrt((i.g + i.h) ** 2 + 4 * w * (w - 1) * i.h ** 2))
            elif version == "PWXD":
                if i.h > i.g:
                    i.f = i.g + i.h  # W* pwXD
                else:
                    i.f = (i.g + 2 * (w - 1) * i.h) / w
            else:
                if i.g < (2 * w - 1) * i.h:
                    i.f = i.g + i.h  # W* pwXU
                else:
                    i.f = (i.g + i.h) / w
            '''
            (1/2*w)*(i.g+(2*w-1)*i.h+sqrt((i.g-i.h)*2+4*w*i.g*i.h)) W* XDP
            (1/2*w)*(i.g+i.h+sqrt((i.g+i.h)**2 +4*w*(w-1)*i.h**2)) W* XUP
            if i.h>i.g:
                i.f=i.g+i.h                       # W* pwXD
            else:
                i.f=(i.g+2*(w-1)*i.h)/w
            if i.g<(2*w-1)*i.h:
                i.f=i.g+i.h                       # W* pwXU
            else:
                i.f=(i.g+i.h)/w
            '''

            for open_node in open_list:
                if i == open_node and i.g > open_node.g:
                    continue
            if i not in open_list:
                open_list.append(i)


'''
(106, 94) (6, 36)
(105, 92) (4, 37)
(5, 36) (106, 94)
(6, 36) (106, 90)
(105, 94) (3, 37)
(8, 72) (7, 36)
(6, 37) (8, 72)
(8, 71) (7, 37)
(8, 71) (6, 35)
(9, 71) (8, 37)
'''
version = ["XDP", "PWXD", "PWXU"]
duree = []
listetraj1 = [[(106, 92), (4, 37)], [(105, 93), (6, 36)], [(105, 92), (3, 36)], [(104, 91), (4, 36)], [(4, 36), (105, 92)]]
listetraj2 = [[(9, 74), (5, 36)], [(3, 72), (4, 36)], [(6, 73), (4, 39)], [(4, 36), (7, 71)], [(6, 72), (5, 39)]]
listetraj3 = [[(72, 74), (65, 48)], [(71, 74), (64, 49)], [(61, 51), (59, 74)], [(73, 50), (67, 73)], [(65, 48), (78, 74)]]
nbressai=20
listetraj=listetraj2
for essai in range(1,nbressai+1):
    for k in range(1, 10):
        for j in range(len(version)):
            for i in range(len(listetraj)):
                t1 = time.time()

                astar(labi, listetraj[i][0], listetraj[i][1], i, len(listetraj), version[j], k,essai)
                t2 = time.time()
                duree.append(t2 - t1)
                # enregistrement(version[j],t2-t1)
            enregistrement(version[j], sum(duree) / len(duree), k)
            duree = []
con.close()

print("fait")