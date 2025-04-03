#!/usr/bin/python3

def initialise_tableau(taille):
    tab = [0 for i in range(taille)]
    return tab


def saisir_valeurs(tableau, taille):
    return True

def somme(tableau):
    som = 0
    for i in range(len(tableau)):
        som += tableau[i]
    return som
        
def moyenne(tableau):
    som = somme(tableau)
    return som/len(tableau)

# pour validation, ne pas modifier
def test():
    print("Tests initialisation/saisie/parcours !")
    assert initialise_tableau(2) ==  [0,0], "Initialisation à revoir"
    assert initialise_tableau(5) ==  [0,0,0,0,0], "Initialisation à revoir"
    print("Les tests d'initialisation sont OK !")

    assert somme([0,0,0,0,0]) == 0, "La somme d'un tableau composé de 0 est à revoir"
    assert somme([0,0,0,1,0]) == 1, "La somme est fausse !"
    assert somme([0,0,0,1,0,1]) == 2, "La somme est fausse !"
    assert somme([12, -10]) == 2, "La somme est fausse !"
    print("Les tests de somme sont OK !")

    assert(moyenne([0,0,0,0,0])) == 0, "La moyenne est fausse !"
    assert(moyenne([10,10,10,10,10])) == 10, "La moyenne est fausse !"
    assert(moyenne([0, 20, 10])) == 10, "La moyenne est fausse !"

    print("Tous les tests sont OK !")

test()