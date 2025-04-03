#!/usr/bin/python3

def appliquer_cycle(tableau,cycle):
  ...

def test_appliquer_cycle():
  print('Test de la fonction appliquer_cycle')
  assert appliquer_cycle([11,12,13],[])==[11,12,13]
  assert appliquer_cycle([11,12,13,14],[2])==[11,12,13,14]
  assert appliquer_cycle([11,12,13,14,15,16],[2,5,1])==[11,16,12,14,15,13]
  assert appliquer_cycle([11,12,13,14,15,16],[4,3,1,2,0,5])==[13,14,12,15,16,11]
  print('  OK')

test_appliquer_cycle()
