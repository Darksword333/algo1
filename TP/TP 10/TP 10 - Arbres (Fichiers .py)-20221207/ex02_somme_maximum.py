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
def calculer_somme(arbre):
    if est_vide(arbre):
        return 0
    somme = racine(arbre) + calculer_somme(gauche(arbre)) + calculer_somme(droite(arbre))
    return somme 

def test_calculer_somme():
  print('Test de la fonction calculer_somme')
  assert calculer_somme(None)==0
  assert calculer_somme((7,None,None))==7
  # 8 ──────────┐
  #       ┌──── 3
  #    ┌─ 9 ─┐
  #    1     7
  assert calculer_somme((8,None,(3,(9,(1,None,None),(7,None,None)),None)))==28
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert calculer_somme((3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None)))==59
  print('  OK')

def calculer_maximum(arbre):
    if est_vide(arbre):
        return 0
    maximumg = calculer_maximum(gauche(arbre))
    maximumd = calculer_maximum(droite(arbre))
    return max(maximumg, maximumd, racine(arbre))

def test_calculer_maximum():
  print('Test de la fonction calculer_maximum')
  assert calculer_maximum((7,None,None))==7
  # 8 ──────────┐
  #       ┌──── 3
  #    ┌─ 9 ─┐
  #    1     7
  assert calculer_maximum((8,None,(3,(9,(1,None,None),(7,None,None)),None)))==9
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert calculer_maximum((3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None)))==8
  print('  OK')

test_calculer_somme()
test_calculer_maximum()
