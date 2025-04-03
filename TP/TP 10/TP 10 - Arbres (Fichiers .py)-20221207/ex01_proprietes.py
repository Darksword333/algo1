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
def calculer_taille(arbre):
    if est_vide(arbre):
      return 0
    taille  = calculer_taille(gauche(arbre)) + calculer_taille(droite(arbre)) + 1
    return taille

def test_calculer_taille():
  print('Test de la fonction calculer_taille')
  assert calculer_taille(None)==0
  assert calculer_taille((8,None,None))==1
  assert calculer_taille((3,(6,None,None),None))==2
  assert calculer_taille((7,None,(1,None,None)))==2
  assert calculer_taille((3,(5,None,None),(4,None,None)))==3
  #          ┌────────── 3 ─┐
  #    ┌──── 8 ────┐        5 ────┐
  # ┌─ 2 ─┐     ┌─ 7 ─┐        ┌─ 6 ─┐
  # 5     4     1     3        7     8
  assert calculer_taille((3,(8,(2,(5,None,None),(4,None,None)),(7,(1,None,None),(3,None,None))),(5,None,(6,(7,None,None),(8,None,None),None),None)))==12
  print('  OK')

def calculer_hauteur(arbre):
    if est_vide(arbre):
        return 0
    hauteurgauche = calculer_hauteur(gauche(arbre)) + 1
    hauteurdroite = calculer_hauteur(droite(arbre)) + 1
    if hauteurgauche >= hauteurdroite:
        return hauteurgauche
    if hauteurdroite >= hauteurgauche:
        return hauteurdroite

def test_calculer_hauteur():
  print('Test de la fonction calculer_hauteur')
  assert calculer_hauteur(None)==0
  assert calculer_hauteur((8,None,None))==1
  assert calculer_hauteur((3,(6,None,None),None))==2
  assert calculer_hauteur((7,None,(1,None,None)))==2
  assert calculer_hauteur((3,(5,None,None),(4,None,None)))==2
  # 8 ──────────┐
  #       ┌──── 3
  #    ┌─ 9 ─┐
  #    1     7
  assert calculer_hauteur((8,None,(3,(9,(1,None,None),(7,None,None)),None)))==4
  # 5 ─┐
  #    1 ───────────────────┐
  #                      ┌─ 5 ─┐
  #       ┌───────────── 8     5
  #       9 ────┐
  #          ┌─ 9 ────┐
  #          5     ┌─ 8
  #                8
  assert calculer_hauteur((5,None,(1,None,(5,(8,(9,None,(9,(5,None,None),(8,(8,None,None),None))),None),(5,None,None)))))==8
  print('  OK')

test_calculer_taille()
test_calculer_hauteur()
