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
def convertir_en_chaine(liste):
  ...

def test_convertir_en_chaine():
  print('test de la fonction convertir_en_chaine')
  assert convertir_en_chaine(None)=='', 'erreur liste vide'
  assert convertir_en_chaine((10,None))=='10 ', 'erreur singleton'
  assert convertir_en_chaine((1,(2,(4,(5,(7,(8,None)))))))=='1 2 4 5 7 8 ', 'erreur cas general'
  print('  OK')

test_convertir_en_chaine()
