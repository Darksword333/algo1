#!/usr/bin/python3

import time

def puissance_A(a,n):
  r = 1
  p = n
  while p>0:
    r = r*a
    p = p-1
  return r

def puissance_B(a,n):
  r = 1
  x = a
  p = n
  while p>0:
    if p%2==1:
      r = r*x
    p = p//2
    x = x*x
  return r

a = 54


def mesure_temps_puissancea():
    tic = 0
    tac = 0
    i = 0
    while i != 9 :
        i+=1
        tic,tac = 0,0
        tic = time.time()
        puissance_A(10, i)
        tac = time.time()
        print(i)
        print(tac-tic)
        
def mesure_temps_puissanceb():
    tic = 0
    tac = 0
    i = 0
    while i != 9 :
        i+=1
        tic,tac = 0,0
        tic = time.time()
        puissance_B(10, i)
        tac = time.time()
        print(i)
        print(tac-tic)
        
print("Mesure du temps en seconde de puissance_A :")
mesure_temps_puissancea()
print("Mesure du temps en seconde de puissance_B :")
mesure_temps_puissanceb()