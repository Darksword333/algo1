#!/usr/bin/python3

# FONCTIONS DE BASE
def creer_liste_vide():
  return None

def creer_liste(t,q):
  return t,q

def tete(liste):
  return liste[0]

def queue(liste):
  return liste[1]

def est_vide(liste):
  return liste==None

# FONCTIONS PLUS EVOLUEES
def nombre_elements(liste):
    compteur = 0
    if est_vide(liste):
        return compteur
    compteur = compteur + 1 + nombre_elements(queue(liste))
    return compteur

def test_nombre_elements():
  print("test de la fonction nombre_elements")
  assert nombre_elements(None)==0, "erreur liste vide"
  assert nombre_elements((5,None))==1, "erreur liste à 1 élément"
  assert nombre_elements((5,(9,(10,(-1,None)))))==4, "erreur liste à 4 éléments"
  print("  OK")

def lire_element(liste,i):
    indice = 0 
    if est_vide(liste):
        return 0
    if tete(liste) == i:
        return indice
    indice = indice + 1 + lire_element(queue(liste), i)
    return indice

def test_lire_element():
  print("test de la fonction lire_element")
  liste = (4,(2,(8,(9,(10,None)))))
  assert lire_element(liste,0)==4, "erreur indice 0"
  assert lire_element(liste,1)==2, "erreur indice 1"
  assert lire_element(liste,2)==8, "erreur indice 2"
  assert lire_element(liste,3)==9, "erreur indice 3"
  assert lire_element(liste,4)==10, "erreur indice 4"
  print("  OK")

def ecrire_element(liste,i,valeur):
  ...

def test_ecrire_element():
  print("test de la fonction ecrire_element")
  assert ecrire_element((4,(2,(8,(9,(10,None))))),0,7)==(7,(2,(8,(9,(10,None))))), "erreur indice 0"
  assert ecrire_element((7,(2,(8,(9,(10,None))))),2,3)==(7,(2,(3,(9,(10,None))))), "erreur indice 2"
  assert ecrire_element((7,(2,(3,(9,(10,None))))),4,8)==(7,(2,(3,(9,(8,None))))), "erreur indice 4"
  print("  OK")

test_nombre_elements()
test_lire_element()
test_ecrire_element()
