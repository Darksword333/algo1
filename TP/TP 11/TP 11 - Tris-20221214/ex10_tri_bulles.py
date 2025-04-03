#!/usr/bin/python3
import random, time

def permutation_aleatoire(n):
  permutation = list(range(n))
  random.shuffle(permutation)
  return permutation

def tri_bulles_etape(tab,i):
  ...

def test_tri_bulles_etape():
  print('Test de la fonction tri_bulles_etape')
  assert tri_bulles_etape([1],1)==[1]
  assert tri_bulles_etape([2,1],2)==[1,2]
  assert tri_bulles_etape([1,2,0],3)==[1,0,2]
  assert tri_bulles_etape([1,0,2],2)==[0,1,2]
  assert tri_bulles_etape([0,1,2],1)==[0,1,2]
  assert tri_bulles_etape([2,1,3,0],4)==[1,2,0,3]
  assert tri_bulles_etape([1,2,0,3],3)==[1,0,2,3]
  assert tri_bulles_etape([1,0,2,3],2)==[0,1,2,3]
  assert tri_bulles_etape([0,1,2,3],1)==[0,1,2,3]
  assert tri_bulles_etape([2,0,-1,4,3,6,7,9],5)==[0,-1,2,3,4,6,7,9]
  print('  OK')

def tri_bulles(tab):
  ...

def test_tri_bulles():
  print('Test de la fonction tri_bulles')
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
    assert tri_bulles(tab[:])==sorted(tab), 'erreur : {}'.format(tab)
  print('  OK')

test_tri_bulles_etape()
test_tri_bulles()

for k in range(13):
  n = 10**k
  tab = permutation_aleatoire(n)
  # /!\ ATTENTION /!\
  # Ne pas mettre la création du tableau aléatoire entre tic et tac
  # (sinon la mesure est faussée)
  ...
  print(f'n=10^{k} : {tac-tic} sec')

