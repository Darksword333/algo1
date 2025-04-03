#!/usr/bin/python3

def matrice_produit(colonne,ligne):
    produit = []
    for i in range(len(colonne)):
        produit.append(0*len(ligne))
    for j in range(len(colonne)):
        for i in range(len(ligne)):
            produit[j][i].append(ligne[i]*colonne[j])
    return
            

def test_matrice_produit():
  print('Test de la fonction matrice_produit')
  assert matrice_produit([2],[3])==[[6]], 'erreur 1'
  assert matrice_produit([1,2],[3,4])==[[3,4],[6,8]], 'erreur 2'
  assert matrice_produit([1,3,2],[4,6,5])==[[4,6,5],[12,18,15],[8,12,10]], 'erreur 3'
  assert matrice_produit([1,3],[4,6,5])==[[4,6,5],[12,18,15]], 'erreur 4'
  assert matrice_produit([7,8,-2,9],[1,-3,4,-5])==[[7,-21,28,-35],[8,-24,32,-40],[-2,6,-8,10],[9,-27,36,-45]], 'erreur 5'
  assert matrice_produit([7,8,-2],[1,-3,4,-5])==[[7,-21,28,-35],[8,-24,32,-40],[-2,6,-8,10]], 'erreur 6'
  print('  OK')

test_matrice_produit()
