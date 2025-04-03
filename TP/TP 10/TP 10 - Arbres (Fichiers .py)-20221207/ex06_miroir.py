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

# EXERCICES
def miroir(arbre):
  ...

def test_miroir():
  print('Test de la fonction miroir')
  assert miroir(None)==None
  assert miroir((5,None,None))==(5,None,None)
  assert miroir((2,(6,None,None),None))==(2,None,(6,None,None))
  assert miroir((1,None,(4,None,None)))==(1,(4,None,None),None)
  # ┌─ 0 ─┐
  # 2     7
  assert miroir((0,(2,None,None),(7,None,None)))==(0,(7,None,None),(2,None,None))
  # 0 ──────────┐
  #       ┌──── 1
  #    ┌─ 2 ─┐
  #    3     4
  assert miroir((0,None,(1,(2,(3,None,None),(4,None,None)),None)))== (0,(1,None,(2,(4,None,None),(3,None,None))),None)
  #           ┌──────────── 16 ──────────┐
  #    ┌───── 5 ─────┐             ┌──── 7 ─────┐
  # ┌─ 4 ──┐     ┌─ 10 ──┐      ┌─ 6 ─┐      ┌─ 1 ──┐
  # 2     11     8      14      3     9     15     12
  assert miroir((16,(5,(4,(2,None,None),(11,None,None)),(10,(8,None,None),(14,None,None))),(7,(6,(3,None,None),(9,None,None)),(1,(15,None,None),(12,None,None)))))==(16,(7,(1,(12,None,None),(15,None,None)),(6,(9,None,None),(3,None,None))),(5,(10,(14,None,None),(8,None,None)),(4,(11,None,None),(2,None,None))))
  print('  OK')

test_miroir()
