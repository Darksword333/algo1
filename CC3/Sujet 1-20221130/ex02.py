#!/usr/bin/python3

def est_symetrique(matrice):
    taille_ligne = len(matrice[0])
    taille_colonne = len(matrice)
    val = 0
    sym = False
    if taille_colonne == 1 and taille_ligne == 1:
        sym = True
        return sym
    elif taille_colonne == 1 and taille_ligne != 1:
        return False
    for i in range(taille_colonne-1):
        for j in range(1, taille_ligne):
            if matrice[i][j] == matrice[i+1][j-1]:
                sym = True    
            else :
                return False
    return sym

def test_est_symetrique():
  print('Test de la fonction est_symetrique')
  assert est_symetrique([[8]]), 'erreur 1'
  assert not est_symetrique([[1,3],[2,1]]), 'erreur 2'
  assert est_symetrique([[1,3],[3,2]]), 'erreur 3'
  assert est_symetrique([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]), 'erreur 4'
  assert not est_symetrique([[7,1,2],[1,7,2],[7,2,1]]), 'erreur 5'
  assert not est_symetrique([[7,1,2],[1,7],[7,2,1]]), 'erreur 6'
  assert not est_symetrique([[1, 6661]]), 'erreur 7'
  print('  OK')


test_est_symetrique()
