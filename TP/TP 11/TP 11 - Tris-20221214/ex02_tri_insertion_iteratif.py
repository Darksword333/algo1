#!/usr/bin/python3

def permuter(tab,i,j):
  tab[i],tab[j] = tab[j],tab[i]

def est_trie(tab,i):
  for j in range(1,i):
    if tab[j]<tab[j-1]:
      return False
  return True

def tri_insertion(tab):
    assert True, 'Pre-condition'
    i = 0
    j = i
    assert est_trie(tab,i), 'Invariant'
    while i < len(tab):
        while j > 0:
            if tab[j] < tab[j-1]:
                permuter(tab, j, j-1)
            j -= 1
        assert est_trie(tab,i), 'Invariant'
        i += 1
        j=i
    assert est_trie(tab,len(tab)), 'Post-condition'
    return tab

def test_tri_insertion():
  print('Test de la fonction tri_insertion')
  tableaux = [
    [],
    [0],
    [2,1],
    [1,2],
    [3,2,1],
    [1,3,2],
    [1,4,6,7],
    [16,12,3,-2],
    [1,3,3,5,0,4,4,5]
  ]
  for tab in tableaux:
    assert tri_insertion(tab[:])==sorted(tab), 'erreur : {}'.format(tab)
  print('  OK')

test_tri_insertion()

'''
def tri_insertion(tab):
    assert True, 'Pre-condition'
    i = 0
    jmin=i
    print(tab)
    assert est_trie(tab,i), 'Invariant'
    while i < len(tab):
        for j in range(i, len(tab)):
            if tab[j] < tab[jmin]:
                jmin = j
        for j in range(jmin, i, -1):
            if tab[j] > tab[jmin]:
                permuter(tab, j, jmin)
                jmin = j
        assert est_trie(tab,i), 'Invariant'
        i+= 1 
        jmin = i
    assert est_trie(tab,len(tab)), 'Post-condition'
    return tab
'''