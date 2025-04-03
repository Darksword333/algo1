# FONCTIONS AUXILIAIRES

def est_infegal(tab,g,d,m):
  ...

def est_sup(tab,g,d,m):
  ...

def permuter(tab,i,j):
  ...

# EXERCICE

def partitionner_pivot(tab):
  n = len(tab)
  assert n>0, 'Pre-condition'
  pivot = tab[0] # ne pas modifier
  ...
  assert (
    0<=i_pivot<=j<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,j+1,n,pivot)
  ), 'Invariant (initialisation)'
  while ...:
    ...
    assert (
      0<=i_pivot<=j<n and tab[i_pivot]==pivot
      and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,j+1,n,pivot)
    ), 'Invariant (itération)'
  assert (
    0<=i_pivot<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,i_pivot+1,n,pivot)
  ), 'Post-condition'
  return i_pivot,tab

def test_partitionner_pivot():
  print('Test de la fonction partitionner_pivot')
  assert partitionner_pivot([8])==(0,[8])
  assert partitionner_pivot([8,7])==(1,[7,8])
  assert partitionner_pivot([1,2,3])==(0,[1,3,2])
  assert partitionner_pivot([5,4,3,2,1])==(4,[4,3,2,1,5])
  assert partitionner_pivot([4,4,5,1,7,2,6])==(3,[4,2,1,4,7,6,5])
  assert partitionner_pivot([8,7,6,5,4,4,4,1,2,3])==(9,[7,6,5,4,4,4,1,2,3,8])
  assert partitionner_pivot([9,4,6,13,4,2,9,8,11,10,5])==(7,[4,6,5,4,2,9,8,9,10,11,13])
  assert partitionner_pivot([4,4,4,4,4,4,4,4,4,4,4,4,4,4,4])==(14,[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4])
  print('  OK')

test_partitionner_pivot()