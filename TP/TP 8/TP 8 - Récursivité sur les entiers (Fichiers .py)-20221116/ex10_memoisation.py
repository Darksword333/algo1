def fibonacci(n):
  if n<=1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)


def test_fibonacci():
  print('Test de la fonction fibonacci')
  assert fibonacci(0)==0
  assert fibonacci(1)==1
  assert fibonacci(2)==1
  assert fibonacci(3)==2
  assert fibonacci(4)==3
  assert fibonacci(5)==5
  assert fibonacci(6)==8
  assert fibonacci(7)==13
  print('  OK pour les petits nombres')
  print('  ...')
  assert fibonacci(100)==354224848179261915075
  print('  OK pour les grands nombres')

test_fibonacci()
