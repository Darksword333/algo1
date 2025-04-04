#!/usr/bin/python3
import random
import time

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(0,n)
  return tab

def somme_maximale(tab):
  n = len(tab)
  maximum = tab[0]+tab[1]
  for i in range(n):
    for j in range(i+1,n):
      if tab[i]+tab[j]>maximum:
        maximum = tab[i]+tab[j]
  return maximum

def test_somme_maximale():
  print('Test de la fonction somme_maximale')
  assert somme_maximale([3,7])==10
  assert somme_maximale([8,2,4])==12
  assert somme_maximale([8,13,2,13,7,1])==26
  assert somme_maximale([9,6,12,11,9,3,17,1,19,0])==36
  assert somme_maximale([-9,-9,14,-18,5,-8,-9,11,10,-3])==25
  print('  OK')

test_somme_maximale()


def mesure_temps_somme_maximale():
    tic = 0
    tac = 0
    i = 1
    while i != 9 :
        i+=1
        tic,tac = 0,0
        tic = time.time()
        somme_maximale(tableau_aleatoire(i))
        tac = time.time()
        print(i)
        print(tac-tic)
        
print("Mesure du temps en seconde de somme_maximale :")
mesure_temps_somme_maximale()

