def bebes(n):
  ...

def adultes(n):
  ...

def test_lapins():
  print('Test des fonctions bebes et adultes')
  assert bebes(0)==0 and adultes(0)==1
  assert bebes(1)==1 and adultes(1)==1
  assert bebes(2)==1 and adultes(2)==2
  assert bebes(3)==2 and adultes(3)==3
  assert bebes(4)==3 and adultes(4)==5
  assert bebes(5)==5 and adultes(5)==8
  assert bebes(6)==8 and adultes(6)==13
  print('  OK')

test_lapins()
