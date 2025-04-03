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
def premier_indice(liste,valeur):
  ...

def test_premier_indice():
  print('Test de la fonction premier_indice')
  assert premier_indice(None,7)==-1, 'erreur liste vide'
  assert premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),7)==-1, 'erreur valeur absente'
  assert premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),3)==0, 'erreur valeur debut'
  assert premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),2)==6, 'erreur valeur fin'
  assert premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),6)==2, 'erreur valeur 6'
  assert premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),5)==1, 'erreur valeur 5'
  print('  OK')

test_premier_indice()
