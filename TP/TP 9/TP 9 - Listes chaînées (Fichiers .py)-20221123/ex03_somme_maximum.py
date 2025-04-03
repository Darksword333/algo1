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
def somme(liste):
  ...

def test_somme():
  print("test de la fonction somme")
  assert somme(None)==0, "erreur 0"
  assert somme((6,None))==6, "erreur 1"
  assert somme((7,(4,(-2,(3,None)))))==12, "erreur 2"
  print("  OK")


def maximum(liste):
  ...

def test_maximum():
  print("test de la fonction maximum")
  assert maximum((6,None))==6, "erreur 1"
  assert maximum((7,(4,(-2,(3,None)))))==7, "erreur 2"
  assert maximum((7,(4,(-2,(8,(3,None))))))==8, "erreur 3"
  assert maximum((7,(4,(-2,(8,(3,(19,None)))))))==19, "erreur 3"
  assert maximum((63,(82,(84,(81,(71,(14,(52,(38,(5,(23,(38,(26,(66,(22,(10,(64,(48,(63,(57,(3,(23,(72,(45,(78,(99,(100,(90,(83,(47,(36,(37,(62,(8,(16,(89,(56,(48,(71,(83,(89,None)))))))))))))))))))))))))))))))))))))))))==100, "erreur 4"
  print("  OK")

test_somme()
test_maximum()
