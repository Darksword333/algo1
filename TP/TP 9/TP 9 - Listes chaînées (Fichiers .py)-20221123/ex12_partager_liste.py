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
def partager_liste(liste):
  ...

def test_partager_liste():
  print("test de la fonction partager_liste")
  assert partager_liste(None)==(None,None), "erreur liste vide"
  assert partager_liste((4,None))==((4,None),None), "erreur liste 1 element"
  assert partager_liste((5,(6,None)))==((5,None),(6,None)), "erreur liste 2 elements"
  assert partager_liste((9,(8,(7,None))))==((9,(7,None)),(8,None)), "erreur liste 3 elements"
  assert partager_liste((10,(2,(6,(4,(7,(3,(1,(5,None)))))))))==((10,(6,(7,(1,None)))),(2,(4,(3,(5,None))))), "erreur cas general"
  print("  OK")

test_partager_liste()
