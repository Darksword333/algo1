def division_euclidienne(x,y):
    assert x>=0 and y>0, 'Pre-Condition'
    q = 0
    r = x
    assert q>=0 and x>=0, 'Invariant Initialisation'
    while r>=y:
        v_debut = r
        assert v_debut>=0, 'Variant positif'
        q += 1
        r -= y
        v_fin = r
        assert v_fin<v_debut, 'Variant décroissant'
        assert r<=x, 'Invariant Itération'
    assert r<y and r<=x, 'Post-Condition'
    return q, r

def test_division_euclidienne():
  print('Test de la fonction division_euclidienne')
  assert division_euclidienne(43,10)==(4,3)
  assert division_euclidienne(0,10)==(0,0)
  assert division_euclidienne(10,5)==(2,0)
  assert division_euclidienne(5,36)==(0,5)
  assert division_euclidienne(125,4)==(31,1)
  assert division_euclidienne(6661,1)==(6661,0)
  print('  OK')

test_division_euclidienne()