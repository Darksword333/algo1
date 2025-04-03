#!/usr/bin/python3

def somme_deux_a_deux(tableau):
    for i in range(len(tableau)-1):
        tableau[i] = tableau[i] + tableau[i+1]
    tableau.pop()
    return tableau


def test_somme_deux_a_deux():
    print('Test de la fonction somme_deux_a_deux')
    assert somme_deux_a_deux([1, 2, 3, 4]) == [3, 5, 7]
    assert somme_deux_a_deux([3, 1]) == [4]
    assert somme_deux_a_deux([4, 7, 3, -8, 2]) == [11, 10, -5, -6]
    assert somme_deux_a_deux([7, -3, 2, 9, 11, -6]) == [4, -1, 11, 20, 5]
    assert somme_deux_a_deux([-5, 3, 0, 0, -1, 5, -5, 7]
                             ) == [-2, 3, 0, -1, 4, 0, 2]
    print('  OK')


def somme_glissante(tableau, n):
    tab = []
    for i in range(len(tableau)):
        if 


def test_somme_glissante():
    print('Test de la fonction somme_glissante Q2')
    assert somme_glissante([1, 7, 8, -2], 1) == [1, 7, 8, -2]
    assert somme_glissante([1, 7, 8, -2], 2) == [8, 15, 6]
    assert somme_glissante([1, 7, 8, -2], 3) == [16, 13]
    assert somme_glissante([1, 7, 8, -2], 4) == [14]
    print('  OK')
    print('Test de la fonction somme_glissante optimisée Q3')
    assert somme_glissante([1]*199999, 100000) == [100000]*100000
    print('  OK')


test_somme_deux_a_deux()
test_somme_glissante()
