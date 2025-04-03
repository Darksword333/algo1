def sont_chiffres_croissants(n):
    croissant = False
    if n == 0:
        return True
    if n//10 <= n%10:
        croissant = True
        return croissant
    sont_chiffres_croissants(n//10)
    return croissant
#Problème car n n'est pas forcement a 2 chiffre mais plus


def test_sont_chiffres_croissants():
  print('Test de la fonction sont_chiffres_croissants')
  assert sont_chiffres_croissants(0)==True
  assert sont_chiffres_croissants(1)==True
  assert sont_chiffres_croissants(9)==True
  assert sont_chiffres_croissants(10)==False
  assert sont_chiffres_croissants(11)==True
  assert sont_chiffres_croissants(12)==True
  assert sont_chiffres_croissants(1111222234555567777888999)==True
  assert sont_chiffres_croissants(11112222345555657777888999)==False
  assert sont_chiffres_croissants(6661)==False

  print('  OK')

test_sont_chiffres_croissants()