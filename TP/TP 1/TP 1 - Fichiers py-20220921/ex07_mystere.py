

def mystere(liste,n):
  ...

def test_mystere():
  print('Test de la fonction mystere')
  assert mystere([],0)==[]
  assert mystere([],7)==[]
  assert mystere([],-5)==[]
  assert mystere([9],0)==[9]
  assert mystere([9],7)==[9]
  assert mystere([9],-5)==[9]
  assert mystere([7,4],0)==[7,4]
  assert mystere([7,4],13)==[4,7]
  assert mystere([7,4],-6)==[7,4]
  assert mystere([9,5,10],0)==[9,5,10]
  assert mystere([9,5,10],1)==[5,10,9]
  assert mystere([9,5,10],2) == [10,9,5]
  assert mystere([9,5,10],3) == [9,5,10]
  assert mystere([9,5,10],4) == [5,10,9]
  assert mystere([9,5,10],-1)==[10,9,5]
  assert mystere([8,5,6,13,2,8],0)==[8,5,6,13,2,8]
  assert mystere([8,5,6,13,2,8],1)==[5,6,13,2,8,8]
  assert mystere([8,5,6,13,2,8],-1)==[8,8,5,6,13,2]
  assert mystere([8,5,6,13,2,8],5)==[8,8,5,6,13,2]
  assert mystere([8,5,6,13,2,8],-5)==[5,6,13,2,8,8]
  assert mystere([8,5,6,13,2,8],6)==[8,5,6,13,2,8]
  assert mystere([8,5,6,13,2,8],42)==[8,5,6,13,2,8]
  assert mystere([8,5,6,13,2,8],-666)==[8,5,6,13,2,8]
  assert mystere([8,5,6,13,2,8],60000000000000000000000000000)==[8,5,6,13,2,8]
  print('  OK')

test_mystere()