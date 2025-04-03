#!/usr/bin/python3

# EXERCICE
def somme_chiffres_impairs(n):
    if n <= 0:
        return 0
    saven = n%10
    somme = 0
    if saven%2 == 1:
        somme += saven
    somme+= somme_chiffres_impairs(n//10)
    return somme


def test_somme_chiffres_impairs():
  print("test de la fonction somme")
  assert somme_chiffres_impairs(13) == 4, "erreur 0"
  assert somme_chiffres_impairs(2124322) == 4, "erreur 1"
  assert somme_chiffres_impairs(22222) == 0, "erreur 2"
  assert somme_chiffres_impairs(0) == 0, "erreur 3"
  assert somme_chiffres_impairs(1111111111) == 10 , "erreur 4"
  assert somme_chiffres_impairs(777) == 21, "erreur 5"
  assert somme_chiffres_impairs(6663) == 3, "erreur 6"
  print("  OK")


test_somme_chiffres_impairs()
