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
def distance_entre_mots(mot1,mot2):
  ...

def test_distance_entre_mots():
  print('Test de la fonction distance_entre_mots')
  assert distance_entre_mots('','ggd')==3
  assert distance_entre_mots('ddgd','')==4
  assert distance_entre_mots('gdd','ddgd')==7
  assert distance_entre_mots('dg','gggggd')==8
  assert distance_entre_mots('dgdggg','dgddgg')==6
  assert distance_entre_mots('ggdgdgdd','ggdgdggddd')==6
  print('  OK')

def chemin_vers_valeur(arbre,valeur):
  ...

def test_chemin_vers_valeur():
  print('Test de la fonction chemin_vers_valeur')
  assert chemin_vers_valeur(None,7)==None
  arbre1 = (8,None,None)
  assert chemin_vers_valeur(arbre1,7)==None
  assert chemin_vers_valeur(arbre1,8)==''
  arbre2 = (9,(8,None,None),(3,None,None))
  # ┌─ 9 ─┐
  # 8     3
  assert chemin_vers_valeur(arbre2,7)==None
  assert chemin_vers_valeur(arbre2,9)==''
  assert chemin_vers_valeur(arbre2,8)=='g'
  assert chemin_vers_valeur(arbre2,3)=='d'
  arbre3 = (16,(5,(4,(2,None,None),(11,None,None)),(10,(8,None,None),(14,None,None))),(7,(6,(3,None,None),(9,None,None)),(1,(15,None,None),(12,None,None))))
  #           ┌──────────── 16 ──────────┐
  #    ┌───── 5 ─────┐             ┌──── 7 ─────┐
  # ┌─ 4 ──┐     ┌─ 10 ──┐      ┌─ 6 ─┐      ┌─ 1 ──┐
  # 2     11     8      14      3     9     15     12
  assert chemin_vers_valeur(arbre3,13)==None
  assert chemin_vers_valeur(arbre3,16)==''
  assert chemin_vers_valeur(arbre3,2)=='ggg'
  assert chemin_vers_valeur(arbre3,12)=='ddd'
  assert chemin_vers_valeur(arbre3,8)=='gdg'
  assert chemin_vers_valeur(arbre3,15)=='ddg'
  print('  OK')

def distance_dans_arbre(arbre,valeur1,valeur2):
  ...

def test_distance_dans_arbre():
  print('Test de la fonction distance_dans_arbre')
  arbre = (16,(5,(4,(2,None,None),(11,None,None)),(10,(8,None,None),(14,None,None))),(7,(6,(3,None,None),(9,None,None)),(1,(15,None,None),(12,None,None))))
  #           ┌──────────── 16 ──────────┐
  #    ┌───── 5 ─────┐             ┌──── 7 ─────┐
  # ┌─ 4 ──┐     ┌─ 10 ──┐      ┌─ 6 ─┐      ┌─ 1 ──┐
  # 2     11     8      14      3     9     15     12
  assert distance_dans_arbre(arbre,8,13)==-1
  assert distance_dans_arbre(arbre,13,8)==-1
  assert distance_dans_arbre(arbre,16,16)==0
  assert distance_dans_arbre(arbre,6,6)==0
  assert distance_dans_arbre(arbre,8,8)==0
  assert distance_dans_arbre(arbre,7,1)==1
  assert distance_dans_arbre(arbre,11,4)==1
  assert distance_dans_arbre(arbre,16,9)==3
  assert distance_dans_arbre(arbre,10,4)==2
  assert distance_dans_arbre(arbre,1,14)==5
  print('  OK')

test_distance_entre_mots()
test_chemin_vers_valeur()
test_distance_dans_arbre()
