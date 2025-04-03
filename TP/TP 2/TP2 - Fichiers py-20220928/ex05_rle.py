#!/usr/bin/python3

import random

def decompresser_liste(liste_compressee):
  ...

def test_decompresser_liste():
  print('Test de la fonction decompresser_liste')
  assert decompresser_liste([])==[]
  assert decompresser_liste([1,2])==[2]
  assert decompresser_liste([5,2])==[2,2,2,2,2]
  assert decompresser_liste([2,1,4,8,4,-3,3,7])==[1,1,8,8,8,8,-3,-3,-3,-3,7,7,7]
  assert decompresser_liste([2,1,4,8,4,-3,3,7,9])==None
  assert decompresser_liste([2,1,4,8,0,-3,3,7])==None
  assert decompresser_liste([2,1,4,8,4,-3,3,-3])==None
  print('  OK')

def compresser_liste(liste):
  assert True, 'Pre-condition'
  ...
  assert decompresser_liste(liste_compressee)==liste, 'Post-condition'
  return liste_compressee

def test_compresser_liste():
  print('Test de la fonction decompresser_liste')
  assert compresser_liste([])==[]
  assert compresser_liste([2])==[1,2]
  assert compresser_liste([2,2,2,2,2])==[5,2]
  assert compresser_liste([1,1,8,8,8,8,-3,-3,-3,-3,7,7,7])==[2,1,4,8,4,-3,3,7]
  # Génération de liste aléatoire
  for _ in range(100):
    liste = []
    for _ in range(random.randint(1,100)):
      liste += [random.randint(-100,100)]*random.randint(1,100)
    compresser_liste(liste)
  print('  OK')

test_decompresser_liste()
test_compresser_liste()

image = [
  255,255,255,255,255,255,255,255,
  255,255,255,255,255,255,255,255,
  255,127,0  ,0  ,0  ,0  ,127,255,
  255,0  ,0  ,127,255,0  ,0  ,255,
  255,0  ,255,255,255,255,0  ,255,
  255,0  ,0  ,127,127,0  ,0  ,255,
  255,127,0  ,0  ,0  ,0  ,127,255,
  255,255,255,255,255,255,255,255
]
...
