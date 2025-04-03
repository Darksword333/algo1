#!/usr/bin/python3

import time

def somme_entiers_1(n):
  somme = 0
  for i in range(1,n+1):
    somme += i
  return somme

def somme_entiers_2(n):
  somme = n*(n+1)//2
  return somme

def mesure_temps_somme1():
    tic = 0
    tac = 0
    i = 0
    while i != 9 :
        i+=1
        tic,tac = 0,0
        tic = time.time()
        somme_entiers_1(10**i)
        tac = time.time()
        print(i)
        print(tac-tic)

def mesure_temps_somme2():
    tic = 0
    tac = 0
    i = 0
    while i != 9 :
        i+=1
        tic,tac = 0,0
        tic = time.time()
        somme_entiers_2(10**i)
        tac = time.time()
        print(i)
        print(tac-tic)
        
print("Mesure du temps en seconde de somme_entiers_1 :")
mesure_temps_somme1()
print("Mesure du temps en seconde de somme_entiers_2 :")
mesure_temps_somme2()