#!/usr/bin/python3

def eliminer_doublons(liste):
  i = 1
  while i<len(liste):
    if liste[i]==liste[i-1] :
      liste.pop(i)
    else :
        i+=1
  return liste


def test_eliminer_doublons():
  print('Test de la fonction eliminer_doublons')
  assert eliminer_doublons([])==[]
  assert eliminer_doublons([7])==[7]
  assert eliminer_doublons([7,7])==[7]
  assert eliminer_doublons([7,9,10,2])==[7,9,10,2]
  assert eliminer_doublons([7,7,9,10,2])==[7,9,10,2]
  assert eliminer_doublons([7,9,10,2,2])==[7,9,10,2]
  assert eliminer_doublons([7,9,9,10,2])==[7,9,10,2]
  assert eliminer_doublons([7,9,9,10,9,9])==[7,9,10,9]
  assert eliminer_doublons([7,7,9,9,10,10,2,2])==[7,9,10,2]
  assert eliminer_doublons([7,7,7])==[7]
  print('  OK')

test_eliminer_doublons()

'''Exercice 1
1) La situation qui a été oublié dans test_eliminer_doublons
est le cas ou il y a plus de deux entiers identiques consécutif
identiques'''
    
