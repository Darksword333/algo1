#!/usr/bin/python3

def est_palindrome(mot):
  debut = 0
  fin = len(mot) - 1
  while debut < fin:
    if not mot[debut] == mot[fin]:
      return False
    debut += 1
    fin -= 1
  return True


def test_palindrome():
  print('Test de la fonction palindrome')
  assert est_palindrome("kayak")
  assert est_palindrome("a")
  assert not est_palindrome("abc")
  assert est_palindrome('1111')
  print('  OK')

test_palindrome()


'''Exercice 1
1) La situation qui a été oublié dans test_palindrome est
le cas ou le nombre de caractère est pair'''
    
