#!/usr/bin/python3

def transposer(matrice):
    mat = [0]*len(matrice[0])
    if len(matrice) == 1: #cas ligne
        for i in range(len(matrice[0])):
            mat[i] = [matrice[0][i]]
        return mat
    elif len(matrice[0]) == 1: #cas colonne
        mat = [0]*len(matrice)
        for i in range(len(matrice)):
            mat[i] = matrice[i][0]
        return [mat]
    for i in range(len(matrice[0])):
        mat[i]= [matrice[0][i], matrice[1][i]]
    print(mat)
    return mat
        

'''
def transposer(matrice):
    if len(matrice[0]) > len(matrice):
        mat = [0]*len(matrice[0])
        for i in range(len(matrice[0])):
            for j in range(len(matrice)):
                mat[i] = matrice[j][i]
        return mat
    return matrice
'''
  
def test_transposer():
  print('Test de la fonction transposer')
  assert transposer([[1]])==[[1]], 'erreur matrice à un élément'
  assert transposer([[4,7,3,-8,2]])==[[4],[7],[3],[-8],[2]], 'erreur matrice ligne'
  assert transposer([[4],[7],[3],[-8],[2]])==[[4,7,3,-8,2]] , 'erreur matrice colonne'
  assert transposer([[1,2,3,4],[2,3,4,5]])==[[1,2],[2,3],[3,4],[4,5]], 'erreur cas général 1'
  assert transposer([[1,2],[2,3],[3,4],[4,5]])==[[1,2,3,4],[2,3,4,5]], 'erreur cas général 2'
  assert transposer([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[[1,5,9],[2,6,10],[3,7,11],[4,8,12]], 'erreur cas général 3'
  assert transposer([[1,5,9],[2,6,10],[3,7,11],[4,8,12]])==[[1,2,3,4],[5,6,7,8],[9,10,11,12]], 'erreur cas général 4'
  assert transposer([[6663, 3]])==[[6663], [3]], 'erreur cas général 5'
  print('  OK')

test_transposer()
