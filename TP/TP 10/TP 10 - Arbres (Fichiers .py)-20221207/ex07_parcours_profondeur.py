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
def parcours_profondeur_prefixe(arbre):
  ...

def test_parcours_profondeur_prefixe():
  print('Test de la fonction parcours_profondeur_prefixe')
  assert parcours_profondeur_prefixe(None)==[]
  arbre1 = (7,None,None)
  assert parcours_profondeur_prefixe(arbre1)==[7]
  arbre2 = (3,(5,None,None),(4,None,None))
  # ┌─ 3 ─┐
  # 5     4
  assert parcours_profondeur_prefixe(arbre2)==[3,5,4]
  arbre3 = (3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None))
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert parcours_profondeur_prefixe(arbre3)==[3,8,2,5,4,7,1,3,5,6,7,8]
  print('  OK')

def parcours_profondeur_infixe(arbre):
  ...

def test_parcours_profondeur_infixe():
  print('Test de la fonction parcours_profondeur_infixe')
  assert parcours_profondeur_infixe(None)==[]
  arbre1 = (7,None,None)
  assert parcours_profondeur_infixe(arbre1)==[7]
  arbre2 = (3,(5,None,None),(4,None,None))
  # ┌─ 3 ─┐
  # 5     4
  assert parcours_profondeur_infixe(arbre2)==[5,3,4]
  arbre3 = (3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None))
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert parcours_profondeur_infixe(arbre3)==[5,2,4,8,1,7,3,3,5,7,6,8]
  print('  OK')

def parcours_profondeur_suffixe(arbre):
  ...

def test_parcours_profondeur_suffixe():
  print('Test de la fonction parcours_profondeur_suffixe')
  assert parcours_profondeur_suffixe(None)==[]
  arbre1 = (7,None,None)
  assert parcours_profondeur_suffixe(arbre1)==[7]
  arbre2 = (3,(5,None,None),(4,None,None))
  # ┌─ 3 ─┐
  # 5     4
  assert parcours_profondeur_suffixe(arbre2)==[5,4,3]
  arbre3 = (3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None))
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert parcours_profondeur_suffixe(arbre3)==[5,4,2,1,3,7,8,7,8,6,5,3]
  print('  OK')

test_parcours_profondeur_prefixe()
test_parcours_profondeur_infixe()
test_parcours_profondeur_suffixe()
