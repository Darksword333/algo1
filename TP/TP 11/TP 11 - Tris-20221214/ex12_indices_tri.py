#!/usr/bin/python3

def indices_tri(tableau):
  ...
  

def test_indices_tri():
  print('Test de la fonction indices_tri')
  assert indices_tri([6])==[0]
  assert indices_tri([5,8])==[0,1]
  assert indices_tri([8,4])==[1,0]
  assert indices_tri([3,5,8])==[0,1,2]
  assert indices_tri([3,8,5])==[0,2,1]
  assert indices_tri([5,3,8])==[1,0,2]
  assert indices_tri([8,3,5])==[1,2,0]
  assert indices_tri([5,8,3])==[2,0,1]
  assert indices_tri([8,5,3])==[2,1,0]
  assert indices_tri([4,1,8,6,2,3,0,9,5,7])==[6,1,4,5,0,8,3,9,2,7]
  print('  OK')

test_indices_tri()
