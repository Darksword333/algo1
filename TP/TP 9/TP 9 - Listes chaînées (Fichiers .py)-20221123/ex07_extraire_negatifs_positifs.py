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
def extraire_negatifs_positifs(liste):
  ...
  
def test_extraire_negatifs_positifs():
  print("test de la fonction extraire_negatifs_positifs")
  assert extraire_negatifs_positifs(None)==(None,None), "erreur 0"
  assert extraire_negatifs_positifs((-7,None))==((-7,None),None), "erreur 1n"
  assert extraire_negatifs_positifs((0,None))==(None,(0,None)), "erreur 1z"
  assert extraire_negatifs_positifs((6,None))==(None,(6,None)), "erreur 1p"
  assert extraire_negatifs_positifs((-2,(11,(4,(3,(-6,None))))))==((-2,(-6,None)),(11,(4,(3,None)))), "erreur 2"
  assert extraire_negatifs_positifs((16,(-6,(2,(-7,(0,(9,None)))))))==((-6,(-7,None)),(16,(2,(0,(9,None))))), "erreur 3"
  print("  OK")

test_extraire_negatifs_positifs()
