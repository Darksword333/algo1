#!/usr/bin/python3

# FONCTIONS DE BASE
def creer_liste_vide():
  return None

def creer_liste(t,q):
  return t,q

def tete(liste):
  return liste[0]

def queue(liste):
  return liste[1]

def est_vide(liste):
  return liste==None

# EXERCICE
def ajouter_element_fin(liste,valeur):
    if est_vide(liste):
        return creer_liste(valeur, creer_liste_vide())
    return creer_liste(tete(liste), ajouter_element_fin(queue(liste), valeur))

def test_ajouter_element_fin():
  print("test de la fonction ajouter_element_fin")
  assert ajouter_element_fin(None,-6)==(-6,None), "erreur 1"
  assert ajouter_element_fin((-6,None),3)==(-6,(3,None)), "erreur 2"
  assert ajouter_element_fin((-6,(3,None)),7)==(-6,(3,(7,None))), "erreur 3"
  print("  OK")

def inserer_element(liste,i,valeur):
    if est_vide(liste):
        return creer_liste(valeur, creer_liste_vide())
    if i == 0:
        return creer_liste(tete(liste), creer_liste(valeur, queue(liste)))
    return creer_liste(tete(liste), inserer_element(queue(liste), i-1, valeur))

def test_inserer_element():
  print("test de la fonction inserer_element")
  assert inserer_element(None,0,-6)==(-6,None), "erreur 1"
  assert inserer_element((-6,None),0,3)==(3,(-6,None)), "erreur 2"
  assert inserer_element((3,(-6,None)),1,7)==(3,(7,(-6,None))), "erreur 3"
  assert inserer_element((3,(7,(-6,None))),3,9)==(3,(7,(-6,(9,None)))), "erreur 4"
  print("  OK")

def supprimer_element(liste,i):
  ...

def test_supprimer_element():
  print("test de la fonction supprimer_element")
  assert supprimer_element((7,(4,(2,(3,None)))),2)==(7,(4,(3,None))), "erreur 1"
  assert supprimer_element((7,(4,(3,None))),2)==(7,(4,None)), "erreur 2"
  assert supprimer_element((7,(4,None)),0)==(4,None), "erreur 3"
  assert supprimer_element((4,None),0)==None, "erreur 4"
  print("  OK")

test_ajouter_element_fin()
test_inserer_element()
test_supprimer_element()
