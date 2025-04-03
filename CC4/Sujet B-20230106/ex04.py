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


def partitionner_negatifs_positifs(liste):
    if est_vide(liste):
        return creer_liste_vide(), creer_liste_vide()
    appel = partitionner_negatifs_positifs(queue(liste))
    if tete(liste) < 0:
        list2 = creer_liste(tete(liste), appel[0])
        appel[1]
    else :
        list2 = creer_liste(tete(liste), appel[1])
        appel[0]
    if tete(list2) >= 0:
        return (appel[0], list2)
    else :
        return (list2, appel[1])


def test_partitionner_negatifs_positifs():
    print('Test de la fonction partitionner_negatifs_positifs')
    assert partitionner_negatifs_positifs(None) == (None, None)
    assert partitionner_negatifs_positifs((4, None)) == (None, (4, None))
    assert partitionner_negatifs_positifs((-5, None)) == ((-5, None), None)
    assert partitionner_negatifs_positifs((0, None)) == (None, (0, None))
    assert partitionner_negatifs_positifs((-8, (10, (17, (-9, None))))) == ((-8, (-9, None)),   (10, (17, None)))
    assert partitionner_negatifs_positifs((-4, (-3, (-8, (-2, (-5, None)))))) == ((-4, (-3, (-8, (-2, (-5, None))))),   None)
    assert partitionner_negatifs_positifs((44, (33, (88, (22, (55, None)))))) == (None,   (44, (33, (88, (22, (55, None))))))
    assert partitionner_negatifs_positifs((-4, (-3, (0, (-2, (55, None)))))) == ((-4, (-3, (-2, None))),   (0, (55, None)))
    print('  OK')


test_partitionner_negatifs_positifs()
