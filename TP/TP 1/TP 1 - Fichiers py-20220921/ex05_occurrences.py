#!/usr/bin/python3

def nb_occurrences(liste,valeur):
  nb = 0
  for e in liste:
    if e==valeur:
      nb += 1
  # affichage pour couverture des tests
  if liste==[]:
    print('|X| | | | | | | | |')
  elif liste==[valeur]:
    print('| |X| | | | | | | |')
  elif len(liste)==1:
    print('| | |X| | | | | | |')
  elif len(liste)>=5:
    if nb==0:
      print('| | | |X| | | | | |')
    elif nb==1:
      if liste[0]==valeur:
        print('| | | | |X| | | | |')
      elif liste[-1]==valeur:
        print('| | | | | |X| | | |')
      else:
        print('| | | | | | |X| | |')
    elif nb<len(liste):
      print('| | | | | | | |X| |')
    else:
      print('| | | | | | | | |X|')
  #
  return nb

def test_nb_occurrences():
  print('Test de la fonction nb_occurrences')
  assert nb_occurrences([], 5)
  assert nb_occurrences([7], 7)
  assert nb_occurrences([9], 4)
  assert nb_occurrences([1,3,9,5,7], 2)
  assert nb_occurrences([1,3,9,5,7], 1)
  assert nb_occurrences([1,3,9,5,7], 7)
  assert nb_occurrences([1,3,9,5,7], 9)
  assert nb_occurrences([1,3,9,5,7,5], 5)
  assert nb_occurrences([2,2,2,2,2], 2)
  print('  OK')

test_nb_occurrences()
