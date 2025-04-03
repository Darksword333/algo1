#!/usr/bin/python3

def minimum_local(matrice, i, j):
  ...

def test_minimum_local():
  print('Test de la fonction minimum_local')
  matrice = [
    [4, 5, 6, 3, 2],
    [3, 6, 4, 1, 2],
    [5, 4, 9, 6, 7],
    [0, 8, 7, 4, 3],
  ]
  assert minimum_local(matrice,2,1)==0, 'erreur cas général 1'
  assert minimum_local(matrice,2,2)==1, 'erreur cas général 2'
  assert minimum_local(matrice,1,3)==1, 'erreur cas général 3'
  assert minimum_local(matrice,1,0)==3, 'erreur bord gauche'
  assert minimum_local(matrice,2,4)==1, 'erreur bord droite'
  assert minimum_local(matrice,0,1)==3, 'erreur bord haut'
  assert minimum_local(matrice,3,3)==3, 'erreur bord bas'
  #
  assert minimum_local([[8]],0,0)==8
  print('  OK')

test_minimum_local()
