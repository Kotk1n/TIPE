from math import *
import time
class Case():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
#il faut transformer les blocs en les point de pixelisation .

#fonction qui retourne True si l'individu se dirige dans le bon sens , False si l'individu se dirige à contre-sens , None sinon.
def sens(caseparent,caseenfant,zonefleches):

    for i in range(len(zonefleches)):
        if caseenfant in zonefleches[i][0]:
            direction=zonefleches[i][1]

            if direction=="nord":
                if (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]-1):
                    return True
                elif caseenfant[1]==caseparent[1]+1:
                    return False
                else:
                    return None
            elif direction=="Nord-est":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]-1):
                    return True

                elif (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]) or (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]+1) or (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]+1):
                    return False
                else:
                    return None
            elif direction=="est":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]):
                    return(True)
                elif caseenfant[0]==caseparent[0]-1:
                    return (False)
                else:return None
            elif direction=="sud-est":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]+1):
                    return True
                elif (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]) or (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]-1) or (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]-1):
                    return False
                else:return None
            elif direction=="sud":
                if (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]+1):
                    return(True)
                elif caseenfant[1]==caseparent[1]-1:
                    return (False)
                else: return None
            elif direction=="sud-ouest":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]+1):
                    return True
                elif (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]-1) or (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]-1) or (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]):
                    return False
                else:
                    return None
            elif direction=="ouest":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]):
                    return True
                elif caseenfant[0]== caseparent[0]+1:
                    return False
                else: return None
            elif direction=="nord-ouest":
                if (caseenfant[0],caseenfant[1])==(caseparent[0]-1,caseparent[1]-1):
                    return True
                elif (caseenfant[0],caseenfant[1])==(caseparent[0],caseparent[1]+1) or (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]+1) or (caseenfant[0],caseenfant[1])==(caseparent[0]+1,caseparent[1]):
                    return False
                else: return None
            else:
                print("problème avec la direction")
                return None



def astar(labi, debut, fin,pointfait,pointot,zonefleches):
    print(debut, fin)
    w=2

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

#Boucle jusque case d'arrivée
    while len(open_list) > 0:



        caseactuelle = open_list[0]
        current_numero = 0
        for numero, case in enumerate(open_list):
            if case.f < caseactuelle.f:
                caseactuelle = case
                current_numero = numero

        #Rajoute la case traitée à la closed liste
        open_list.pop(current_numero)
        closed_list.append(caseactuelle)

        # Vérifie arrivée
        if caseactuelle == arrivee:
            chemin = []
            current = caseactuelle
            while current is not None:
                chemin.append(current.position) #remonte la liste des cases parcourues
                current = current.parent
            return chemin[::-1]  #retourne la liste

        # génère enfant
        enfant = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0),(1,1),(1,-1),(-1,-1),(-1,1)]: # cases à coté ,


            case_pos = (caseactuelle.position[0] + new_position[0], caseactuelle.position[1] + new_position[1])

            # Vérification bien dans labi
            if case_pos[0] > (len(labi) - 1) or case_pos[0] < 0 or case_pos[1] > (len(labi[len(labi) - 1]) - 1) or case_pos[1] < 0:
                continue

            # Vérifie que pas un obstacle
            if labi[case_pos[0]][case_pos[1]] ==0:
                print("recherche du chemin",pointfait,"sur",pointot)

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

            i.f=(1/2*w)*(i.g+(2*w-1)*i.h+sqrt((i.g-i.h)*2+4*w *i.g*i.h)) #W* XDP

            indsens = sens(caseactuelle.position, i.position, zonefleches)


            if indsens == True:
                i.f =i.f
            elif indsens == False:
                i.f = i.f



            '''
            (1/2*w)*(i.g+(2*w-1)*i.h+sqrt((i.g-i.h)*2+4*w *i.g*i.h)) W* XDP
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










def main():
    global path
    path =[]





if __name__ == '__main__':
    main()

