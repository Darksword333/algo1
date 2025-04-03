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
def sont_egales(liste1,liste2):
  ...

def test_sont_egales():
  print("test de la fonction sont_egales")
  assert sont_egales(None,None), "erreur 1"
  assert not sont_egales(None,(6,None)), "erreur 2"
  assert sont_egales((6,None),(6,None)), "erreur 3"
  assert not sont_egales((6,None),(8,None)), "erreur 4"
  assert not sont_egales((7,(5,None)),(8,None)), "erreur 5"
  assert not sont_egales((7,(5,None)),(7,(5,(8,(6,(1,(0,None))))))), "erreur 6"
  assert sont_egales((7,(5,(8,(6,(1,(0,None)))))),(7,(5,(8,(6,(1,(0,None))))))), "erreur 7"
  assert not sont_egales((7,(5,(8,(6,(1,(0,None)))))),(7,(5,(8,(2,(1,(0,None))))))), "erreur 8"
  print("  OK")

test_sont_egales()
