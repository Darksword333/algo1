
def somme_chiffres(n):
    somme = 0
    if n == 0:
        return 0
    somme = n%10 + somme_chiffres(n//10)
    return somme

def test_somme_chiffres():
  print('Test de la fonction somme_chiffres')
  assert somme_chiffres(0)==0
  assert somme_chiffres(1)==1
  assert somme_chiffres(9)==9
  assert somme_chiffres(20)==2
  assert somme_chiffres(83)==11
  assert somme_chiffres(24654)==21
  assert somme_chiffres(251740385)==35
  print('  OK')

def premier_chiffre(n):
    prems = 0
    if n < 10:
        return n
    prems = premier_chiffre(n//10)
    return prems

def test_premier_chiffre():
  print('Test de la fonction premier_chiffre')
  assert premier_chiffre(0)==0
  assert premier_chiffre(1)==1
  assert premier_chiffre(9)==9
  assert premier_chiffre(20)==2
  assert premier_chiffre(83)==8
  assert premier_chiffre(24654)==2
  assert premier_chiffre(251740385)==2
  print('  OK')

def occurences_chiffre(n,c):
    occu = 0
    if n < 10:
        if n == c:
            return 1
        else : 
            return 0
    occu += occurences_chiffre(n//10, c)
    occu += occurences_chiffre(n%10, c)
    return occu
      


def test_occurences_chiffre():
  print('Test de la fonction occurences_chiffre')
  assert occurences_chiffre(1,1)==1
  assert occurences_chiffre(1,7)==0
  assert occurences_chiffre(9,9)==1
  assert occurences_chiffre(9,7)==0
  assert occurences_chiffre(20,2)==1
  assert occurences_chiffre(20,1)==0
  assert occurences_chiffre(20,0)==1
  assert occurences_chiffre(24654,4)==2
  assert occurences_chiffre(251740385,0)==1
  assert occurences_chiffre(0,0)==1
  assert occurences_chiffre(0,7)==0
  print('  OK')

test_somme_chiffres()
test_premier_chiffre()
test_occurences_chiffre()
