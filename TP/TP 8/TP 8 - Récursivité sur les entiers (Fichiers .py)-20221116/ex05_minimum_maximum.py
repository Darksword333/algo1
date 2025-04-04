def minimum_chiffres(n):
  if n<10:
    return n
  elif n%10<minimum_chiffres(n//10):
    return n%10
  else:
    return minimum_chiffres(n//10)


def test_minimum_chiffres():
  print('Test de la fonction minimum_chiffres')
  assert minimum_chiffres(0)==0
  assert minimum_chiffres(9)==9
  assert minimum_chiffres(10)==0
  assert minimum_chiffres(3679284655)==2
  assert minimum_chiffres(8979899789)==7
  assert minimum_chiffres(9999999999)==9
  print('  pas encore OK...')
  assert minimum_chiffres(1999999999999999999999999999999999999999999999999999)==1
  print('  OK')

def minimum_maximum_chiffres(n):
  ...

def test_minimum_maximum_chiffres():
  print('Test de la fonction minimum_maximum_chiffres')
  assert minimum_maximum_chiffres(0)==(0,0)
  assert minimum_maximum_chiffres(9)==(9,9)
  assert minimum_maximum_chiffres(10)==(0,1)
  assert minimum_maximum_chiffres(3679284655)==(2,9)
  assert minimum_maximum_chiffres(8979899789)==(7,9)
  assert minimum_maximum_chiffres(9999999999)==(9,9)
  assert minimum_maximum_chiffres(454545454545454545454545454545454364545454545)==(3,6)
  print('  OK')

test_minimum_chiffres()
test_minimum_maximum_chiffres()
