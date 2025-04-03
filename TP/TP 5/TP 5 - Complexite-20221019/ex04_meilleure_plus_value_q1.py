#!/usr/bin/python3

import random

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(-n//2,n//2)
  return tab

def meilleure_plus_value_A(tab):
  n = len(tab)
  difference_max = 0
  for i in range(n):
    for j in range(n):
      if (tab[j]-tab[i])>difference_max and i<=j:
        difference_max = tab[j]-tab[i]
  return difference_max

def meilleure_plus_value_B(tab):
  n = len(tab)
  difference_max = 0
  for i in range(n):
    for j in range(i+1,n):
      if (tab[j]-tab[i])>difference_max:
        difference_max = tab[j]-tab[i]
  return difference_max

