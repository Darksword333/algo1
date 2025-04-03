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
def inverser_rec(liste,liste_inverse):
  ...

def inverser(liste):
  ...

def test_inverser():
  print("test de la fonction inverser")
  assert inverser(None)==None, "erreur liste vide"
  assert inverser((6,None))==(6,None), "erreur liste à 1 élément"
  assert inverser((3,(4,(5,None))))==(5,(4,(3,None))), "erreur liste vide"
  print("  OK")

test_inverser()
