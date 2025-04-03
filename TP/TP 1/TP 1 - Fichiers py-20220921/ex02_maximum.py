#!/usr/bin/python3

def maximum(liste):
  m = liste[0] #il suffit d'initialiser m à une valeur existante de la liste et non 0
  for e in liste:
    if e>m:
      m = e
  return m

def test_maximum():
  print('Test de la fonction maximum')
  assert maximum([10])==10
  assert maximum([15,2,6,0])==15
  assert maximum([8,9,3,12])==12
  assert maximum([1,7,13,4])==13
  assert maximum([-1,-7,-3,-9,-5])==-1
  print('  OK')

test_maximum()

'''Exercice 1
1) La situation qui a été oublié dans test_maximum est
le cas ou les nombres sont négatifs'''
    
