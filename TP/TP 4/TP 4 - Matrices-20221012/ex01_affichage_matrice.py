#!/usr/bin/python3

def affiche(tableau):
    for i in range(len(tableau)):
        print(tableau[i])

# programme principal ne pas modifier
# la validation se fait sur la sortie standard
# pas d'asserts dans cet exercice !
print("- Une grille de morpion...")
morpion=[['o','o','x'],['o','x','o'],['x','o','o']]
affiche(morpion)

print("- portrait de Mr Rio...")
dessin=[[' ','_','_','_',' '],['/','o',' ','o','\\'],['|',' ','L',' ','|'],['\\','_','-','_','/']]
affiche(dessin) 

print("-la matrice identité de R^4")
matrice = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    matrice[i][i] = 1
affiche(matrice) 