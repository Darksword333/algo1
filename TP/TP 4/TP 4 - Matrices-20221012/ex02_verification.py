#!/usr/bin/python3

def est_matrice(matrice):
    for i in range(len(matrice)-1):
      if len(matrice[i]) != len(matrice[i+1]):
          return False
    return True


def test_est_matrice():
  print('Test de la fonction est_matrice')
  assert est_matrice([[]])
  assert est_matrice([[],[],[],[],[]])
  assert est_matrice([[1]])
  assert est_matrice([[4,7,3,-8,2]])
  assert est_matrice([[4],[7],[3],[-8],[2]])
  assert est_matrice([[1,2,3,4],[2,3,4,1]])
  assert est_matrice([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
  assert not est_matrice([[],[7,1],[3,4]])
  assert not est_matrice([[9,7,8],[7,1,2],[]])
  assert not est_matrice([[1,2,3,4],[5,7,8],[9,10,11,12]])
  assert not est_matrice([[1,4],[5,7,8],[9,10,12]])
  assert not est_matrice([[1,4,1],[5,7,8],[9,12]])
  print('  OK')

test_est_matrice()
