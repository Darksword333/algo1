#!/usr/bin/python3

def permuter(tab,i,j):
  tab[i],tab[j] = tab[j],tab[i]

def est_trie(tab,i):
  for j in range(1,i):
    if tab[j]<tab[j-1]:
      return False
  return True

def tri_selection(tab):
    assert True, 'Pre-condition'
    i = 0
    jmin = i
    assert est_trie(tab,i), 'Invariant'
    while i < len(tab):
        for j in range(i, len(tab)):
            if tab[j] < tab[jmin]:
                jmin = j
        permuter(tab, i, jmin)
        i+= 1
        jmin = i
        assert est_trie(tab,i), 'Invariant'
    assert est_trie(tab,len(tab)), 'Post-condition'
    return tab

def test_tri_selection():
  print('Test de la fonction tri_selection')
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
    assert tri_selection(tab[:])==sorted(tab), 'erreur : {}'.format(tab)
  print('  OK')

test_tri_selection()
