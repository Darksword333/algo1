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


def evaluer_expression(arbre):
  ...

def test_evaluer_expression():
  print('Test de la fonction evaluer_expression')
  # expressions bien formées
  # ┌─ + ─┐
  # 3     4
  assert evaluer_expression(('+',('3',None,None),('4',None,None)))==7
  # ┌─ - ─┐
  # 6     1
  assert evaluer_expression(('-',('6',None,None),('1',None,None)))==5
  # ┌─ * ─┐
  # 7     5
  assert evaluer_expression(('*',('7',None,None),('5',None,None)))==35
  # ┌─ // ─┐
  # 8      3
  assert evaluer_expression(('//',('8',None,None),('3',None,None)))==2
  #          ┌──── + ─┐
  #    ┌──── - ─┐     7
  # ┌─ + ─┐     2
  # 3     5
  assert evaluer_expression(('+',('-',('+',('3',None,None),('5',None,None)),('2',None,None)),('7',None,None)))==13
  #    ┌────────── - ─────┐
  # ┌─ + ────┐        ┌─ // ─┐
  # 8     ┌─ * ─┐     9      2
  #       3     5
  assert evaluer_expression(('-',('+',('8',None,None),('*',('3',None,None),('5',None,None))),('//',('9',None,None),('2',None,None))))==19
  #    ┌────────── - ───────────┐
  # ┌─ * ────┐            ┌──── * ─┐
  # 3     ┌─ + ─┐     ┌─ // ─┐     3
  #       5     2     9      2
  assert evaluer_expression(('-',('*',('3',None,None),('+',('5',None,None),('2',None,None))),('*',('//',('9',None,None),('2',None,None)),('3',None,None))))==9
  # Expressions mal formées
  # + ──┐
  #    51
  assert evaluer_expression(('+',None,('51',None,None)))==None
  #  ┌─ +
  # 51
  assert evaluer_expression(('+',('51',None,None),None))==None
  # Division par 0
  # ┌─ // ─┐
  # 1      0
  assert evaluer_expression(('//',('1',None,None),('0',None,None)))==None
  print('  OK')

test_evaluer_expression()
