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
  print('Test de la fonction inserer_dans_liste_triee')
  assert inserer_dans_liste_triee(None,6)==(6,None)
  assert inserer_dans_liste_triee((6,None),3)==(3,(6,None))
  assert inserer_dans_liste_triee((3,(6,None)),4)==(3,(4,(6,None)))
  assert inserer_dans_liste_triee((3,(4,(6,None))),7)==(3,(4,(6,(7,None))))
  assert inserer_dans_liste_triee((3,(4,(6,(7,None)))),1)==(1,(3,(4,(6,(7,None)))))
  print('  OK')

def tri_insertion(liste):
  ...

def test_tri_insertion():
  print('Test de la fonction tri_insertion')
  assert tri_insertion(None)==None
  assert tri_insertion((0,None))==(0,None)
  assert tri_insertion((2,(1,None)))==(1,(2,None))
  assert tri_insertion((1,(2,None)))==(1,(2,None))
  assert tri_insertion((3,(2,(1,None))))==(1,(2,(3,None)))
  assert tri_insertion((1,(3,(2,None))))==(1,(2,(3,None)))
  assert tri_insertion((7,(6,(4,(1,None)))))==(1,(4,(6,(7,None))))
  assert tri_insertion((-2,(12,(3,(16,None)))))==(-2,(3,(12,(16,None))))
  assert tri_insertion((4,(4,(5,(1,(7,(2,(6,None))))))))==(1,(2,(4,(4,(5,(6,(7,None)))))))
  assert tri_insertion((1,(3,(3,(5,(0,(4,(4,(5,None)))))))))==(0,(1,(3,(3,(4,(4,(5,(5,None))))))))
  print('  OK')

test_inserer_dans_liste_triee()
test_tri_insertion()
