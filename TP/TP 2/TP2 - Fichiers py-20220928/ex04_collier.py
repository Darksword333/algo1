#!/usr/bin/python3

import random

def generer_collier_aleatoire(m0,m1):
  collier = [0]*(2*m0)+[1]*(2*m1)
  random.shuffle(collier)
  return collier

def somme(collier,g,d):
  s = 0
  for i in range(g,d):
    s += collier[i]
  return s

def est_collier_valide(collier):
  ...

def test_est_collier_valide():
  print('Test de la fonction est_collier_valide')
  assert est_collier_valide([])==True
  assert est_collier_valide([0,0])==True
  assert est_collier_valide([1,1])==True
  assert est_collier_valide([0,1])==False
  assert est_collier_valide([2,0])==False
  assert est_collier_valide([1,0,0,1])==True
  assert est_collier_valide([2,0,0,2])==False
  assert est_collier_valide([0,0,0,2])==False
  assert est_collier_valide([1,0,0,1,0,0])==True
  assert est_collier_valide([1,0,0,1,1,0,1,0])==True
  assert est_collier_valide([0,0,0,0,1,1,1,1])==True
  assert est_collier_valide([0,1,1,0,1,1,1,1])==True
  assert est_collier_valide([0,0,0,0,0,0,0,0])==True
  assert est_collier_valide([1,0,0,1,0,0,1,0])==False
  assert est_collier_valide([1,1,0,1,1,1,1,1])==False
  print('  OK')

def partager_collier(collier):
  n = len(collier)
  s1 = somme(collier,0,n)
  assert est_collier_valide(collier), 'Pre-condition'
  ...
  assert 0<=i<=n//2 and somme(collier,i,i+n//2)==s1//2, 'Post-condition'
  return i

def test_partager_collier():
  print('Test de la fonction partager_collier')
  assert partager_collier([])==0
  assert partager_collier([1,1]) in [0,1]
  assert partager_collier([1,0,1,0]) in [0,1]
  assert partager_collier([1,1,0,0])==1
  for _ in range(100):
    m0 = random.randint(0,100)
    m1 = random.randint(0,100)
    collier = generer_collier_aleatoire(m0,m1)
    partager_collier(collier)
  print('  OK')
  
test_est_collier_valide()
test_partager_collier()