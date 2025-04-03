#!/usr/bin/python3
import random, time

def permutation_aleatoire(n):
  permutation = list(range(n))
  random.shuffle(permutation)
  return permutation

def tri_selection(tab):
  ...

def test_tri_selection():
  print('Test de la fonction tri_selection')
  tableaux = [
    [],
    [0],
    [2,1],
    [1,2],
    [3,2,1],
    [1,3,2],
    [1,4,6,7],
    [16,12,3,-2],
    [1,3,3,5,0,4,4,5],
    permutation_aleatoire(20)
  ]
  for tab in tableaux:
    assert tri_selection(tab[:])==sorted(tab), 'erreur : {}'.format(tab)
  print('  OK')

test_tri_selection()

for k in range(13):
  n = 10**k
  tab = permutation_aleatoire(n)
  # /!\ ATTENTION /!\
  # Ne pas mettre la création du tableau aléatoire entre tic et tac
  # (sinon la mesure est faussée)
  ...
  print(f'n=10^{k} : {tac-tic} sec')

