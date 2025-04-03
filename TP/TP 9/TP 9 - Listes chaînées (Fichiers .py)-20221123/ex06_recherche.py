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
def rechercher_rec(liste,valeur,indice):
  ...

def rechercher(liste,valeur):
  ...

def test_rechercher():
  print("test de la fonction rechercher")
  assert rechercher(None,7)==None, "erreur liste vide"
  assert rechercher((3,(5,(6,(6,(5,(4,(2,None))))))),7)==None, "erreur valeur absente"
  assert rechercher((3,(5,(6,(6,(5,(4,(2,None))))))),3)==(0,None), "erreur valeur debut"
  assert rechercher((3,(5,(6,(6,(5,(4,(2,None))))))),2)==(6,None), "erreur valeur fin"
  assert rechercher((3,(5,(6,(6,(5,(4,(2,None))))))),6)==(2,(3,None)), "erreur valeur 6"
  assert rechercher((3,(5,(6,(6,(5,(4,(2,None))))))),5)==(1,(4,None)), "erreur valeur 5"
  print("  OK")

test_rechercher()
