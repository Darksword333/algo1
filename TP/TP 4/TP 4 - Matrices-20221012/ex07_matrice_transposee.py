#!/usr/bin/python3

def transposer(matrice):
  ...

  
def test_transposer():
  print('Test de la fonction transposer')
  assert transposer([[1]])==[[1]], 'erreur matrice à un élément'
  assert transposer([[4,7,3,-8,2]])==[[4],[7],[3],[-8],[2]], 'erreur matrice ligne'
  assert transposer([[4],[7],[3],[-8],[2]])==[[4,7,3,-8,2]] , 'erreur matrice colonne'
  assert transposer([[1,2,3,4],[2,3,4,5]])==[[1,2],[2,3],[3,4],[4,5]], 'erreur cas général 1'
  assert transposer([[1,2],[2,3],[3,4],[4,5]])==[[1,2,3,4],[2,3,4,5]], 'erreur cas général 2'
  assert transposer([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[[1,5,9],[2,6,10],[3,7,11],[4,8,12]], 'erreur cas général 3'
  assert transposer([[1,5,9],[2,6,10],[3,7,11],[4,8,12]])==[[1,2,3,4],[5,6,7,8],[9,10,11,12]], 'erreur cas général 4'
  print('  OK')

test_transposer()
