from tkinter import *
from tkinter.messagebox import *
import pygame

Fenetre = Tk()
Largeur = 300
Hauteur = 300
Nombre_ligne = 3
Nombre_colonne = 3
largeur_case = Largeur//Nombre_ligne
hauteur_case = Hauteur//Nombre_colonne
Couleur = "white"
Joueur = 1



def grille(zone, epaisseur, couleur):
    for i in range (Nombre_ligne):
        zone.create_line(0, hauteur_case * (i+1), Largeur, hauteur_case * (i+1), fill = couleur, width = epaisseur)
    for j in range(Nombre_colonne):
        zone.create_line(largeur_case * (j+1), 0, largeur_case * (j+1), Hauteur, fill = couleur, width = epaisseur)
    zone.pack()

def clique(event):
    #Joueur HUMAIN
    coord_x = event.x//largeur_case
    coord_y = event.y//hauteur_case
    if(tab[coord_y][coord_x] == 0):
        attribut_valeur_j(coord_x,coord_y)
    else:
        showinfo("Impossible","Cette case n'est pas valide")
    print("")
    terminal_test_2(tab)
    if(terminal_test(tab)):
        Fenetre.quit()
    liste_dispo= actions()
    for i in range(len(liste_dispo)):
        print(liste_dispo[i])
    affichage()
    print()
    #Joueur ORDI
    coord = minmax()
    attribut_valeur_o(coord[1],coord[0])
    affichage()
    terminal_test_2(tab)
    if(terminal_test(tab)):
        Fenetre.quit()
    
def attribut_valeur_j(coord_x,coord_y):
    #global Joueur
    #if(Joueur == 1):
    tab[coord_y][coord_x] = 1
    print('ok')
    Zone.create_oval((coord_x)*largeur_case + 2, (coord_y)*largeur_case + 2, (coord_x)*largeur_case +  largeur_case - 2 , (coord_y)*largeur_case +  largeur_case - 2, fill = "green")


def attribut_valeur_o(coord_x,coord_y):
    tab[coord_y][coord_x] = 2
    Zone.create_line((coord_x)*largeur_case + 2, (coord_y)*largeur_case + 2, (coord_x)*largeur_case +  largeur_case - 2 , (coord_y)*largeur_case +  largeur_case - 2, fill = "red", width = 3)
    Zone.create_line( (coord_x)*largeur_case + 2,(coord_y)*largeur_case  + largeur_case - 2, (coord_x)*largeur_case +  largeur_case - 2 , (coord_y)*largeur_case + 2, fill = "red", width = 3)
    print('wow')
    
def affichage():
    for i in range(len(tab)):
         print(tab[i][0], tab[i][1],tab[i][2])

def terminal_test_2(tab1):
    ###################################Joueur 1##################################
    #Win sur ligne 1 
    if((tab1[0][0] == tab1[0][1] == tab1[0][2]) and tab1[0][0] == 1):
        
        showinfo("Victoire",("Le joueur "+ str(tab[0][0]) + " gagné la partie"))
        #return [True,1]
    #Win sur ligne 2
    elif((tab1[1][0] == tab1[1][1] == tab1[1][2]) and tab1[1][0] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur ligne 3 
    elif((tab1[2][0] == tab1[2][1] == tab1[2][2]) and tab1[2][0] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur colonne 1 
    elif((tab1[0][0] == tab1[1][0] == tab1[2][0]) and tab1[0][0] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur colonne 2 
    elif((tab1[0][1] == tab1[1][1] == tab1[2][1]) and tab1[0][1] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur colonne 3 
    elif((tab1[0][2] == tab1[1][2] == tab1[2][2]) and tab1[0][2] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur diagonale 1 
    elif((tab1[0][0] == tab1[1][1] == tab1[2][2]) and tab1[0][0] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    #Win sur diagonale 2 
    elif((tab1[0][2] == tab1[1][1] == tab1[2][0]) and tab1[0][2] == 1):
        
        showinfo("Victoire",("Le joueur 1 gagné la partie"))
        #return [True,1]
    
    if(actions() == []):
        
        showinfo("Egalité","Personne n'a su prendre le dessus...")
        #return True

    #########################################Joueur 2###################################################


    #Win sur ligne 1 
    if((tab1[0][0] == tab1[0][1] == tab1[0][2]) and tab1[0][0] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur ligne 2
    elif((tab1[1][0] == tab1[1][1] == tab1[1][2]) and tab1[1][0] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur ligne 3 
    elif((tab1[2][0] == tab1[2][1] == tab1[2][2]) and tab1[2][0] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur colonne 1 
    elif((tab1[0][0] == tab1[1][0] == tab1[2][0]) and tab1[0][0] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur colonne 2 
    elif((tab1[0][1] == tab1[1][1] == tab1[2][1]) and tab1[0][1] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur colonne 3 
    elif((tab1[0][2] == tab1[1][2] == tab1[2][2]) and tab1[0][2] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur diagonale 1 
    elif((tab1[0][0] == tab1[1][1] == tab1[2][2]) and tab1[0][0] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    #Win sur diagonale 2 
    elif((tab1[0][2] == tab1[1][1] == tab1[2][0]) and tab1[0][2] == 2):
        
        showinfo("Victoire",("Le joueur 2 gagné la partie"))
        #return [True,2]
    
    if(actions() == []):
        
        showinfo("Egalité","Personne n'a su prendre le dessus...")
        #return [True,0]
    else :
        return [False,0]



def terminal_test(tab1):
    ###################################Joueur 1##################################
    #Win sur ligne 1 
    if((tab1[0][0] == tab1[0][1] == tab1[0][2]) and tab1[0][0] == 1):
        
        #showinfo("Victoire",("Le joueur "+ str(tab[0][0]) + " gagné la partie"))
        return [True,1]
    #Win sur ligne 2
    elif((tab1[1][0] == tab1[1][1] == tab1[1][2]) and tab1[1][0] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur ligne 3 
    elif((tab1[2][0] == tab1[2][1] == tab1[2][2]) and tab1[2][0] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur colonne 1 
    elif((tab1[0][0] == tab1[1][0] == tab1[2][0]) and tab1[0][0] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur colonne 2 
    elif((tab1[0][1] == tab1[1][1] == tab1[2][1]) and tab1[0][1] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur colonne 3 
    elif((tab1[0][2] == tab1[1][2] == tab1[2][2]) and tab1[0][2] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur diagonale 1 
    elif((tab1[0][0] == tab1[1][1] == tab1[2][2]) and tab1[0][0] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    #Win sur diagonale 2 
    elif((tab1[0][2] == tab1[1][1] == tab1[2][0]) and tab1[0][2] == 1):
        
        #showinfo("Victoire",("Le joueur 1 gagné la partie"))
        return [True,1]
    
    if(actions() == []):
        
        #showinfo("Egalité","Personne n'a su prendre le dessus...")
        return True

    #########################################Joueur 2###################################################


    #Win sur ligne 1 
    if((tab1[0][0] == tab1[0][1] == tab1[0][2]) and tab1[0][0] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur ligne 2
    elif((tab1[1][0] == tab1[1][1] == tab1[1][2]) and tab1[1][0] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur ligne 3 
    elif((tab1[2][0] == tab1[2][1] == tab1[2][2]) and tab1[2][0] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur colonne 1 
    elif((tab1[0][0] == tab1[1][0] == tab1[2][0]) and tab1[0][0] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur colonne 2 
    elif((tab1[0][1] == tab1[1][1] == tab1[2][1]) and tab1[0][1] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur colonne 3 
    elif((tab1[0][2] == tab1[1][2] == tab1[2][2]) and tab1[0][2] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur diagonale 1 
    elif((tab1[0][0] == tab1[1][1] == tab1[2][2]) and tab1[0][0] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    #Win sur diagonale 2 
    elif((tab1[0][2] == tab1[1][1] == tab1[2][0]) and tab1[0][2] == 2):
        
        #showinfo("Victoire",("Le joueur 2 gagné la partie"))
        return [True,2]
    
    if(actions() == []):
        
        #showinfo("Egalité","Personne n'a su prendre le dessus...")
        return [True,0]
    else :
        return [False,0]

def actions():
    L= []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if(tab[i][j] == 0):
                L.append([j,i])
    return L


def utility(tab_test):
    if((terminal_test(tab_test))[0] == True):
        return 1000
    else :
        return -1000

def minmax():
    print(tab)
    liste_minmax = [[0,0,0],[0,0,0],[0,0,0]]
    tab_test = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab_test = tab
            if(tab_test[i][j] != 0):
                liste_minmax[i][j] = -9999
                print(tab)
            else:
                tab_test[i][j] = 1
                liste_minmax[i][j] = utility(tab_test)
                tab_test[i][j] = 0

    print(tab)
    print()
    print(tab_test)
    val_max = -9999
    coord = [-1,-1]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if (liste_minmax[i][j] >= val_max):
                val_max = liste_minmax[i][j]
                coord =[i,j]
    print(liste_minmax)  
    return(coord)



##def jeu():
##    if(Joueur == 2):
##        coord = minmax()
##        attribut_valeur(coord[1],coord[0])
##        if((terminal_test(tab))[0]):
##            showinfo("Victoire",("Le joueur 2 a gagné la partie"))
##            return True
##        else:
##            return False
##    else :
##
##        while(Joueur == 1):
##            print('ok')
##        #Attendre que le joueur 1 clique
##            
##        if((terminal_test(tab))[0]):
##            showinfo("Victoire",("Le joueur 1 a gagné la partie"))
##            return True
##        else:
##            return False




if __name__ == "__main__":

    #pygame.mixer.init()
    #son_main = pygame.mixer.Sound("8bit_song.wav")
    #son_main.play()
    print('oui')
    tab = [[0,0,0],[0,0,0],[0,0,0]]
    Zone =  Canvas(Fenetre, width = Largeur, height = Hauteur, background = Couleur)
    grille(Zone,1,"black")
    Fenetre.bind("<Button-1>",clique)
        
    Fenetre.mainloop()

    
