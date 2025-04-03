def syracuse(n):
  ...

def test_syracuse():
  print('Test de la fonction syracuse')
  assert syracuse(1)==[1]
  assert syracuse(2)==[2, 1]
  assert syracuse(3)==[3, 10, 5, 16, 8, 4, 2, 1]
  assert syracuse(14)==[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
  print('  OK')

test_syracuse()
