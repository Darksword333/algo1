#!/usr/bin/python3
import random,time

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
  print('Test de la fonction partager_liste')
  assert partager_liste(None)==(None,None)
  assert partager_liste((4,None))==((4,None),None)
  assert partager_liste((5,(6,None)))==((5,None),(6,None))
  assert partager_liste((9,(8,(7,None))))==((9,(7,None)),(8,None))
  assert partager_liste((10,(2,(6,(4,(7,(3,(1,(5,None)))))))))==((10,(6,(7,(1,None)))),(2,(4,(3,(5,None)))))
  print('  OK')

def fusionner_listes_triees(liste1,liste2):
  ...

def test_fusionner_listes_triees():
  print('Test de la fonction fusionner_listes_triees')
  assert fusionner_listes_triees(None,(3,(5,(6,None))))==(3,(5,(6,None)))
  assert fusionner_listes_triees((7,(9,(10,None))),None)==(7,(9,(10,None)))
  assert fusionner_listes_triees((1,(6,None)),(3,(8,None)))==(1,(3,(6,(8,None))))
  assert fusionner_listes_triees((1,(2,(4,(5,(7,(8,None)))))),(2,(3,(5,(6,(6,(8,None)))))))==(1,(2,(2,(3,(4,(5,(5,(6,(6,(7,(8,(8,None))))))))))))
  print('  OK')

def tri_fusion(liste):
  ...


def test_tri_fusion():
  print('Test de la fonction tri_fusion')
  assert tri_fusion(None)==None
  assert tri_fusion((0,None))==(0,None)
  assert tri_fusion((2,(1,None)))==(1,(2,None))
  assert tri_fusion((1,(2,None)))==(1,(2,None))
  assert tri_fusion((3,(2,(1,None))))==(1,(2,(3,None)))
  assert tri_fusion((1,(3,(2,None))))==(1,(2,(3,None)))
  assert tri_fusion((7,(6,(4,(1,None)))))==(1,(4,(6,(7,None))))
  assert tri_fusion((-2,(12,(3,(16,None)))))==(-2,(3,(12,(16,None))))
  assert tri_fusion((4,(4,(5,(1,(7,(2,(6,None))))))))==(1,(2,(4,(4,(5,(6,(7,None)))))))
  assert tri_fusion((1,(3,(3,(5,(0,(4,(4,(5,None)))))))))==(0,(1,(3,(3,(4,(4,(5,(5,None))))))))
  print('  OK')

test_partager_liste()
test_fusionner_listes_triees()
test_tri_fusion()

