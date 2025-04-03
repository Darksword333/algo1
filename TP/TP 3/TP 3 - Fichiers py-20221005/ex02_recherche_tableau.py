#!/usr/bin/python3

def recherche(valeur, tableau):
    for i in range(len(tableau)):
        if valeur == tableau[i]:
            return i
    return -1
    
# pour validation, ne pas modifier
def test():
    print("Tests recherche...")
    assert recherche(1, [1]) == 0
    assert recherche(1, [5,4,3,2,1]) == 4
    assert recherche(1, [0,4,3,2,1]) == 4
    assert recherche(1, [1,4,3,2,1]) == 0
    assert recherche(1, [5,4,3,2,4]) == -1

    assert recherche("charizard", ["snorlax", "charizard", "mewtwo","bulbasaur"]) == 1
    assert recherche("kirby", ["snorlax", "charizard", "mewtwo","bulbasaur"]) == -1 # kirby n'est PAS un pokemon...
    assert recherche("c", ["snorlax", "charizard", "mewtwo","bulbasaur"]) == -1

    assert recherche(1, []) == -1
    assert recherche([1,2,3], [[1], [1,2] , [1,2,3], [1,2,3,4]]) == 2
    print("Tous les tests sont OK !")

test()