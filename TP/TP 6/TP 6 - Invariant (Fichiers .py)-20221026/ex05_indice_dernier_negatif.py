#!/usr/bin/python3

def est_croissant(tab):
    croissant = True
    i = 0
    while croissant and i < len(tab):
        if tab[i-1] < tab[i]:
            i+=1
        else :
            croissant = False
    return croissant 
    
def test_est_croissant():
  print('Test de la fonction est_croissant')
  assert est_croissant([])==True
  assert est_croissant([3])==True
  assert est_croissant([3,3])==True
  assert est_croissant([3,5])==True
  assert est_croissant([5,3])==False
  assert est_croissant([-5,-3,-3,0,1,2,2,4])==True
  assert est_croissant([-5,-3,-3,0,1,2,2,1])==False
  assert est_croissant([-2,-3,-3,0,1,2,2,4])==False
  assert est_croissant([-5,-3,-3,0,-1,2,2,4])==False
  print('  OK')

def indice_dernier_negatif_1(tab):
  n = len(tab)
  ...
  assert 0<=i<n-1 and tab[i]<=0<tab[i+1], 'Post-condition'
  return i
  

def indice_dernier_negatif_2(tab):
  n = len(tab)
  ...
  assert 0<=i<n-1 and tab[i]<=0<tab[i+1], 'Post-condition'
  return i

def test_indice_dernier_negatif(version):
  print('Test de la fonction indice_dernier_negatif (version {})'.format(version))
  indice_dernier_negatif = {
    1: indice_dernier_negatif_1,
    2: indice_dernier_negatif_2
  }[version]
  assert indice_dernier_negatif([-1,1])==0
  assert indice_dernier_negatif([0,1])==0
  assert indice_dernier_negatif([0,0,1])==1
  assert indice_dernier_negatif([-4,0,1])==1
  assert indice_dernier_negatif([-4,-3,-2,0,1,1,1])==3
  assert indice_dernier_negatif([-4,-3,-2,-2,-2,1,1,1])==4
  assert indice_dernier_negatif([-4,-3,-2,-1,-1,-1,1])==5
  print('  OK')

test_est_croissant()
test_indice_dernier_negatif(1)
test_indice_dernier_negatif(2)

