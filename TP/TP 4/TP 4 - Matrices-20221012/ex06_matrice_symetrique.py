#!/usr/bin/python3

def est_carree(matrice):
  ...

def test_est_carree():
  print('Test de la fonction est_carree')
  assert est_carree([[8]]), 'erreur 1'
  assert est_carree([[1,3],[2,1]]), 'erreur 2'
  assert est_carree([[7,1,2],[1,7,2],[7,2,1]]), 'erreur 3'
  assert est_carree([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]), 'erreur 4'
  assert not est_carree([[4,6,5],[12,18,15]]), 'erreur 5'
  assert not est_carree([[7,-21,28,-35],[8,-24,32,-40],[-2,6,-8,10]]), 'erreur 6'
  print('  OK')

def est_symetrique(matrice):
  ...

def test_est_symetrique():
  print('Test de la fonction est_symetrique')
  assert est_symetrique([[8]]), 'erreur 1'
  assert not est_symetrique([[1,3],[2,1]]), 'erreur 2'
  assert est_symetrique([[1,3],[3,2]]), 'erreur 3'
  assert est_symetrique([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]), 'erreur 4'
  assert not est_symetrique([[7,1,2],[1,7,2],[7,2,1]]), 'erreur 5'
  print('  OK')

test_est_carree()
test_est_symetrique()
