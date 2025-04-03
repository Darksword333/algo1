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
def calculer_nb_occurrences(arbre,valeur):
    if est_vide(arbre):
        return 0
    cmpt = calculer_nb_occurrences(droite(arbre), valeur) + calculer_nb_occurrences(gauche(arbre), valeur)
    if valeur == racine(arbre):
        cmpt += 1
    return cmpt
    

def test_calculer_nb_occurrences():
  print('Test de la fonction calculer_nb_occurrences')
  assert calculer_nb_occurrences(None,2)==0
  arbre1 = (3,None,None)
  assert calculer_nb_occurrences(arbre1,2)==0
  assert calculer_nb_occurrences(arbre1,3)==1
  arbre2 = (4,(5,None,None),(4,None,None))
  # ┌─ 4 ─┐
  # 5     4 
  assert calculer_nb_occurrences(arbre2,7)==0
  assert calculer_nb_occurrences(arbre2,5)==1
  assert calculer_nb_occurrences(arbre2,4)==2
  arbre3 = (5,None,(1,None,(5,(8,(9,None,(9,(5,None,None),(8,(8,None,None),None))),None),(5,None,None))))
  # 5 ─┐
  #    1 ───────────────────┐
  #                      ┌─ 5 ─┐
  #       ┌───────────── 8     5
  #       9 ────┐
  #          ┌─ 9 ────┐
  #          5     ┌─ 8
  #                8
  assert calculer_nb_occurrences(arbre3,3)==0
  assert calculer_nb_occurrences(arbre3,1)==1
  assert calculer_nb_occurrences(arbre3,9)==2
  assert calculer_nb_occurrences(arbre3,8)==3
  assert calculer_nb_occurrences(arbre3,5)==4
  print('  OK')

test_calculer_nb_occurrences()
