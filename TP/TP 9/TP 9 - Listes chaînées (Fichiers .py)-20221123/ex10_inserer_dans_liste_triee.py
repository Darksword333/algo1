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
def inserer_dans_liste_triee(liste,valeur):
  ...

def test_inserer_dans_liste_triee():
  print("test de la fonction inserer_dans_liste_triee")
  assert inserer_dans_liste_triee(None,6)==(6,None), "erreur 1"
  assert inserer_dans_liste_triee((6,None),3)==(3,(6,None)), "erreur 2"
  assert inserer_dans_liste_triee((3,(6,None)),4)==(3,(4,(6,None))), "erreur 3"
  assert inserer_dans_liste_triee((3,(4,(6,None))),7)==(3,(4,(6,(7,None)))), "erreur 4"
  assert inserer_dans_liste_triee((3,(4,(6,(7,None)))),1)==(1,(3,(4,(6,(7,None))))), "erreur 5"
  print("  OK")

test_inserer_dans_liste_triee()
