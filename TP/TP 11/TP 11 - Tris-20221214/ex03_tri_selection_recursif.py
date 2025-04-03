#!/usr/bin/python3

# FONCTIONS DE BASE
def creer_liste_vide():
    return None


def creer_liste(t, q):
    return t, q


def tete(liste):
    return liste[0]


def queue(liste):
    return liste[1]


def est_vide(liste):
    return liste == None

# EXERCICE


def extraire_minimum(liste):
    if liste == creer_liste_vide():
        return 0
    if 


def test_extraire_minimum():
    print('Test de la fonction extraire_minimum')
    assert extraire_minimum((7, None)) == (7, None)
    assert extraire_minimum((1, (3, None))) == (1, (3, None))
    assert extraire_minimum((3, (1, None))) == (1, (3, None))
    assert extraire_minimum((1, (7, (2, (6, (9, None)))))) == (
        1, (7, (2, (6, (9, None)))))
    assert extraire_minimum((7, (2, (6, (9, (1, None)))))) == (
        1, (7, (2, (6, (9, None)))))
    assert extraire_minimum((2, (7, (1, (6, (9, None)))))) == (
        1, (2, (7, (6, (9, None)))))
    assert extraire_minimum((2, (7, (1, (6, (9, None)))))) == (
        1, (2, (7, (6, (9, None)))))
    print('  OK')


def tri_selection(liste):
    ...


def test_tri_selection():
    print('Test de la fonction tri_selection')
    assert tri_selection(None) == None
    assert tri_selection((0, None)) == (0, None)
    assert tri_selection((2, (1, None))) == (1, (2, None))
    assert tri_selection((1, (2, None))) == (1, (2, None))
    assert tri_selection((3, (2, (1, None)))) == (1, (2, (3, None)))
    assert tri_selection((1, (3, (2, None)))) == (1, (2, (3, None)))
    assert tri_selection((7, (6, (4, (1, None))))) == (1, (4, (6, (7, None))))
    assert tri_selection((-2, (12, (3, (16, None))))
                         ) == (-2, (3, (12, (16, None))))
    assert tri_selection((4, (4, (5, (1, (7, (2, (6, None)))))))) == (
        1, (2, (4, (4, (5, (6, (7, None)))))))
    assert tri_selection((1, (3, (3, (5, (0, (4, (4, (5, None))))))))) == (
        0, (1, (3, (3, (4, (4, (5, (5, None))))))))
    print('  OK')


test_extraire_minimum()
test_tri_selection()
