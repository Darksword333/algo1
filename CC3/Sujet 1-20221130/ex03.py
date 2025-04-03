#!/usr/bin/python3

# FONCTIONS DE BASE (NE PAS MODIFIER)
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


def somme_elements_pairs(liste):
    somme = 0
    if est_vide(queue(liste)):
        return 0
    if tete(liste) % 2 == 0:
        somme += tete(liste)
    somme += somme_elements_pairs(creer_liste(tete(queue(liste)), creer_liste_vide()))
    return somme

def test_somme():
    print("test de la fonction somme")
    assert somme_elements_pairs(None) == 0, "erreur 0"
    assert somme_elements_pairs((6, None)) == 6, "erreur 1"
    assert somme_elements_pairs((7, (4, (-2, (3, None))))) == 2, "erreur 2"
    assert somme_elements_pairs((2, (6661, None))) == 2, "erreur 3"
    print("  OK")


test_somme()
