
def pgcd(a,b):
  ...

def test_pgcd():
  print('Test de la fonction pgcd')
  assert pgcd(1,0)==1
  assert pgcd(167,0)==167
  assert pgcd(167,1)==1
  assert pgcd(81,3)==3
  assert pgcd(81285,23)==1
  assert pgcd(144,84)==12
  assert pgcd(51,9)==3
  assert pgcd(678,13)==1
  print('  OK')

test_pgcd()
