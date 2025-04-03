#!/usr/bin/python3

import random

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(-n//2,n//2)
  return tab

def meilleure_plus_value_C(tab):
  ...

def test_meilleure_plus_value():
  print('Test de la fonction meilleure_plus_value_C')
  assert meilleure_plus_value_C([1])==0
  assert meilleure_plus_value_C([5,2])==0
  assert meilleure_plus_value_C([2,5])==3
  assert meilleure_plus_value_C([5,4,1,-1,-2,-3])==0
  assert meilleure_plus_value_C([4,5,1,-1,-2,-3])==1
  assert meilleure_plus_value_C([1,5,-1,-3,-2,4])==7
  # test de complexité
  meilleure_plus_value_C(tableau_aleatoire(100000))
  print('  OK')

test_meilleure_plus_value()

