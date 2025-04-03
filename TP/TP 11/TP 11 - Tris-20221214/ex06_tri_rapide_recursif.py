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
def partitionner_pivot(liste,pivot):
  ...

def test_partitionner_pivot():
  print('Test de la fonction partitionner_pivot')
  assert partitionner_pivot(None,5)==(None,None)
  assert partitionner_pivot((4,None),5)==((4,None),None)
  assert partitionner_pivot((5,None),5)==((5,None),None)
  assert partitionner_pivot((6,None),5)==(None,(6,None))
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),8)==((4,(3,(8,(2,(5,None))))),None)
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),1)==(None,(4,(3,(8,(2,(5,None))))))
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),4)==((4,(3,(2,None))),(8,(5,None)))
  print('  OK')

def concatener_listes(liste1,liste2):
  ...

def test_concatener_listes():
  print('Test de la fonction concatener_listes')
  assert concatener_listes(None,None)==None
  assert concatener_listes(None,(6,(8,(3,(2,None)))))==(6,(8,(3,(2,None))))
  assert concatener_listes((4,(3,(1,(9,None)))),None)==(4,(3,(1,(9,None))))
  assert concatener_listes((8,(4,None)),(7,(1,None)))==(8,(4,(7,(1,None))))
  print('  OK')

def tri_rapide(liste):
  ...

def test_tri_rapide():
  print('Test de la fonction tri_rapide')
  assert tri_rapide(None)==None
  assert tri_rapide((0,None))==(0,None)
  assert tri_rapide((2,(1,None)))==(1,(2,None))
  assert tri_rapide((1,(2,None)))==(1,(2,None))
  assert tri_rapide((3,(2,(1,None))))==(1,(2,(3,None)))
  assert tri_rapide((1,(3,(2,None))))==(1,(2,(3,None)))
  assert tri_rapide((7,(6,(4,(1,None)))))==(1,(4,(6,(7,None))))
  assert tri_rapide((-2,(12,(3,(16,None)))))==(-2,(3,(12,(16,None))))
  assert tri_rapide((4,(4,(5,(1,(7,(2,(6,None))))))))==(1,(2,(4,(4,(5,(6,(7,None)))))))
  assert tri_rapide((1,(3,(3,(5,(0,(4,(4,(5,None)))))))))==(0,(1,(3,(3,(4,(4,(5,(5,None))))))))
  print('  OK')

test_partitionner_pivot()
test_concatener_listes()
test_tri_rapide()
