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
def arbre_parfait_prefixe(hauteur,debut=0):
  ...

def test_arbre_parfait_prefixe():
  print('Test de la fonction arbre_parfait_prefixe')
  assert arbre_parfait_prefixe(0)==None
  assert arbre_parfait_prefixe(1)==(0,None,None)
  # ┌─ 0 ─┐
  # 1     2
  assert arbre_parfait_prefixe(2)==(0,(1,None,None),(2,None,None))
  #    ┌──── 0 ────┐
  # ┌─ 1 ─┐     ┌─ 4 ─┐
  # 2     3     5     6
  assert arbre_parfait_prefixe(3)==(0,(1,(2,None,None),(3,None,None)),(4,(5,None,None),(6,None,None)))
  #          ┌────────── 0 ────────────┐
  #    ┌──── 1 ────┐            ┌───── 8 ──────┐
  # ┌─ 2 ─┐     ┌─ 5 ─┐      ┌─ 9 ──┐      ┌─ 12 ──┐
  # 3     4     6     7     10     11     13      14
  assert arbre_parfait_prefixe(4)==(0,(1,(2,(3,None,None),(4,None,None)),(5,(6,None,None),(7,None,None))),(8,(9,(10,None,None),(11,None,None)),(12,(13,None,None),(14,None,None))))
  print('  OK')

def arbre_parfait_infixe(hauteur,debut=0):
  ...

def test_arbre_parfait_infixe():
  print('Test de la fonction arbre_parfait_infixe')
  assert arbre_parfait_infixe(0)==None
  assert arbre_parfait_infixe(1)==(0,None,None)
  # ┌─ 1 ─┐
  # 0     2
  assert arbre_parfait_infixe(2)==(1,(0,None,None),(2,None,None))
  #    ┌──── 3 ────┐
  # ┌─ 1 ─┐     ┌─ 5 ─┐
  # 0     2     4     6
  assert arbre_parfait_infixe(3)==(3,(1,(0,None,None),(2,None,None)),(5,(4,None,None),(6,None,None)))
  #          ┌────────── 7 ────────────┐
  #    ┌──── 3 ────┐            ┌──── 11 ──────┐
  # ┌─ 1 ─┐     ┌─ 5 ─┐      ┌─ 9 ──┐      ┌─ 13 ──┐
  # 0     2     4     6      8     10     12      14
  assert arbre_parfait_infixe(4)==(7,(3,(1,(0,None,None),(2,None,None)),(5,(4,None,None),(6,None,None))),(11,(9,(8,None,None),(10,None,None)),(13,(12,None,None),(14,None,None))))
  print('  OK')

def arbre_parfait_suffixe(hauteur,debut=0):
  ...

def test_arbre_parfait_suffixe():
  print('Test de la fonction arbre_parfait_suffixe')
  assert arbre_parfait_suffixe(0)==None
  assert arbre_parfait_suffixe(1)==(0,None,None)
  # ┌─ 2 ─┐
  # 0     1
  assert arbre_parfait_suffixe(2)==(2,(0,None,None),(1,None,None))
  #    ┌──── 6 ────┐
  # ┌─ 2 ─┐     ┌─ 5 ─┐
  # 0     1     3     4
  assert arbre_parfait_suffixe(3)==(6,(2,(0,None,None),(1,None,None)),(5,(3,None,None),(4,None,None)))
  #          ┌────────── 14 ───────────┐
  #    ┌──── 6 ────┐            ┌──── 13 ─────┐
  # ┌─ 2 ─┐     ┌─ 5 ─┐      ┌─ 9 ─┐      ┌─ 12 ──┐
  # 0     1     3     4      7     8     10      11
  assert arbre_parfait_suffixe(4)==(14,(6,(2,(0,None,None),(1,None,None)),(5,(3,None,None),(4,None,None))),(13,(9,(7,None,None),(8,None,None)),(12,(10,None,None),(11,None,None))))
  print('  OK')

def arbre_parfait_largeur(hauteur,debut=0):
  ...

def test_arbre_parfait_largeur():
  print('Test de la fonction arbre_parfait_largeur')
  assert arbre_parfait_largeur(0)==None
  assert arbre_parfait_largeur(1)==(0,None,None)
  # ┌─ 0 ─┐
  # 1     2
  assert arbre_parfait_largeur(2)==(0,(1,None,None),(2,None,None))
  #    ┌──── 0 ────┐
  # ┌─ 1 ─┐     ┌─ 2 ─┐
  # 3     4     5     6
  assert arbre_parfait_largeur(3)==(0,(1,(3,None,None),(4,None,None)),(2,(5,None,None),(6,None,None)))
  #          ┌─────────── 0 ────────────┐
  #    ┌──── 1 ────┐             ┌───── 2 ─────┐
  # ┌─ 3 ─┐     ┌─ 4 ──┐      ┌─ 5 ──┐      ┌─ 6 ──┐
  # 7     8     9     10     11     12     13     14
  assert arbre_parfait_largeur(4)==(0,(1,(3,(7,None,None),(8,None,None)),(4,(9,None,None),(10,None,None))),(2,(5,(11,None,None),(12,None,None)),(6,(13,None,None),(14,None,None))))
  print('  OK')

test_arbre_parfait_prefixe()
test_arbre_parfait_infixe()
test_arbre_parfait_suffixe()
test_arbre_parfait_largeur()
