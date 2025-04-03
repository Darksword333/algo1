def somme_carres(n):
    somme = 0
    if n == 1:
        return 1
    elif n == 0:
        return 0
    somme = n**2 + somme_carres(n-1)
    return somme

def test_somme_carres():
  print('Test de la fonction somme_carres')
  assert somme_carres(0)==0
  assert somme_carres(1)==1
  assert somme_carres(2)==5
  assert somme_carres(10)==385
  assert somme_carres(100)==338350
  print('  OK')

test_somme_carres()
