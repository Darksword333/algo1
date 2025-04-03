#!/usr/bin/python3

# FONCTIONS DE BASE
def creer_arbre_vide():
  return None

def creer_arbre(r,g,d):
  return r,g,d

def racine(arbre):
  return arbre[0]

def gauche(arbre):
  return arbre[1]

def droite(arbre):
  return arbre[2]

def est_vide(arbre):
  return arbre==None

# EXERCICE
def substituer(arbre,ancienne,nouvelle):
  ...

def test_substituer():
  print('Test de la fonction substituer')
  assert substituer(None,3,6)==None
  assert substituer((8,None,None),7,8)==(8,None,None)
  assert substituer((8,None,None),8,7)==(7,None,None)
  assert substituer((3,(5,None,None),(4,None,None)),4,6)==(3,(5,None,None),(6,None,None))
  assert substituer((3,(5,None,None),(4,None,None)),5,6)==(3,(6,None,None),(4,None,None))
  assert substituer((3,(5,None,None),(4,None,None)),3,6)==(6,(5,None,None),(4,None,None))
  # 8 ──────────┐
  #       ┌──── 3
  #    ┌─ 9 ─┐
  #    3     7
  assert substituer((8,None,(3,(9,(3,None,None),(7,None,None)),None)),3,6)==(8,None,(6,(9,(6,None,None),(7,None,None)),None))
  # 5 ─┐
  #    1 ───────────────────┐
  #                      ┌─ 5 ─┐
  #       ┌───────────── 8     5
  #       9 ────┐
  #          ┌─ 9 ────┐
  #          5     ┌─ 8
  #                8
  assert substituer((5,None,(1,None,(5,(8,(9,None,(9,(5,None,None),(8,(8,None,None),None))),None),(5,None,None)))),8,2)==(5,None,(1,None,(5,(2,(9,None,(9,(5,None,None),(2,(2,None,None),None))),None),(5,None,None))))
  print('  OK')

test_substituer()
