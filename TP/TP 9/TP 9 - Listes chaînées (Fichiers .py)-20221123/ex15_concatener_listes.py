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
def concatener_listes(liste1,liste2):
  ...
  
def test_concatener_listes():
  print("test de la fonction concatener_listes")
  assert concatener_listes(None,None)==None, "erreur listes vides"
  assert concatener_listes(None,(6,(8,(3,(2,None)))))==(6,(8,(3,(2,None)))), "erreur liste1 vide"
  assert concatener_listes((4,(3,(1,(9,None)))),None)==(4,(3,(1,(9,None)))), "erreur liste2 vide"
  assert concatener_listes((8,(4,None)),(7,(1,None)))==(8,(4,(7,(1,None)))), "erreur cas général"
  print("  OK")

test_concatener_listes()
