#!/usr/bin/python3
import random
import time


def permutation_aleatoire(n):
    permutation = list(range(n))
    random.shuffle(permutation)
    return permutation


def tri_cocktail_aller(tab, i_gauche, i_droite):
    ...
    # @beginprof
    for j in range(i_gauche+1, i_droite):
        if tab[j-1] > tab[j]:
            tab[j-1], tab[j] = tab[j], tab[j-1]
    return tab
    # @endprof


def test_tri_cocktail_aller():
    print('Test de la fonction tri_cocktail_aller')
    assert tri_cocktail_aller([1], 0, 1) == [1]
    assert tri_cocktail_aller([2, 1], 0, 2) == [1, 2]
    assert tri_cocktail_aller([1, 2, 0], 0, 3) == [1, 0, 2]
    assert tri_cocktail_aller([2, 1, 3, 0], 0, 4) == [1, 2, 0, 3]
    assert tri_cocktail_aller([0, 2, 1, 3], 1, 3) == [0, 1, 2, 3]
    assert tri_cocktail_aller(
        [-1, 6, 0, 4, 7, 3, 2, 9], 1, 7) == [-1, 0, 4, 6, 3, 2, 7, 9]
    assert tri_cocktail_aller(
        [-1, 0, 4, 6, 3, 2, 7, 9], 2, 6) == [-1, 0, 4, 3, 2, 6, 7, 9]
    print('  OK')


def tri_cocktail_retour(tab, i_gauche, i_droite):
    ...
    # @beginprof
    for j in range(i_droite-1, i_gauche, -1):
        if tab[j-1] > tab[j]:
            tab[j-1], tab[j] = tab[j], tab[j-1]
    return tab
    # @endprof


def test_tri_cocktail_retour():
    print('Test de la fonction tri_cocktail_retour')
    assert tri_cocktail_retour([1, 0, 2], 0, 2) == [0, 1, 2]
    assert tri_cocktail_retour([2, 1, 0, 3], 0, 3) == [0, 2, 1, 3]
    assert tri_cocktail_retour(
        [6, -1, 4, 7, 3, 0, 2, 9], 0, 7) == [-1, 6, 0, 4, 7, 3, 2, 9]
    assert tri_cocktail_retour(
        [-1, 3, 6, 4, 0, 2, 7, 9], 1, 6) == [-1, 0, 3, 6, 4, 2, 7, 9]
    assert tri_cocktail_retour(
        [-1, 0, 3, 4, 2, 6, 7, 9], 2, 5) == [-1, 0, 2, 3, 4, 6, 7, 9]
    print('  OK')


def tri_cocktail(tab):
    ...
    # @beginprof
    i_gauche = 0
    i_droite = len(tab)
    est_aller = True
    while i_gauche < i_droite:
        if est_aller:
            tab = tri_cocktail_aller(tab, i_gauche, i_droite)
            i_droite -= 1
        else:
            tab = tri_cocktail_retour(tab, i_gauche, i_droite)
            i_gauche += 1
        est_aller = not est_aller
    return tab


def tri_cocktail(tab):
    i_gauche = 0
    i_droite = len(tab)
    for i in range(len(tab)):
        if i % 2 == 0:
            tab = tri_cocktail_aller(tab, i_gauche, i_droite)
            i_droite -= 1
        else:
            tab = tri_cocktail_retour(tab, i_gauche, i_droite)
            i_gauche += 1
    return tab
    # @endprof


def test_tri_cocktail():
    print('Test de la fonction tri_cocktail')
    tableaux = [
        [],
        [0],
        [2, 1],
        [1, 2],
        [3, 2, 1],
        [1, 3, 2],
        [1, 4, 6, 7],
        [16, 12, 3, -2],
        [1, 3, 3, 5, 0, 4, 4, 5],
        permutation_aleatoire(20)
    ]
    for tab in tableaux:
        assert tri_cocktail(tab[:]) == sorted(tab), 'erreur : {}'.format(tab)
    print('  OK')


test_tri_cocktail_aller()
test_tri_cocktail_retour()
test_tri_cocktail()

for k in range(13):
    n = 10**k
    tab = permutation_aleatoire(n)
    # /!\ ATTENTION /!\
    # Ne pas mettre la création du tableau aléatoire entre tic et tac
    # (sinon la mesure est faussée)
    ...
    # @beginprof
    tic = time.time()
    tab = tri_cocktail(tab)
    tac = time.time()
    # @endprof
    print(f'n=10^{k} : {tac-tic} sec')

# @beginprof
# 1) a) On relève les temps suivants :
# n=10^0 : 1.6689300537109375e-06 sec
# n=10^1 : 9.298324584960938e-06 sec
# n=10^2 : 0.0005304813385009766 sec
# n=10^3 : 0.05826973915100098 sec
# n=10^4 : 5.547476530075073 sec
#
# b) Lorsque n est multiplié par 10, le temps d'exécution semble multiplié par 100.
# La complexité en temps semble donc proportionnelle à n^2 lorsque n devient grand.
#
# c) Dans la fonction tri_cocktail_aller, il y a i_droite-(igauche+1) itérations
# Dans la fonction tri_cocktail_retour, il y a aussi (i_droite-1)-igauche itérations
# Dans les deux cas, il y a i_droite-i_gauche-1 itérations
# A chaque itération de la boucle de la fonction principale tri_cocktail, la
# différence i_droite-i_gauche décroit de 1, donc le nombre total d'itérations est :
# aller  : (n-1)
# retour : (n-2)
# aller  : (n-3)
# retour : (n-4)
# etc.
# le nb total d'itérations est (n-1)n/2
# La complexité en temps est donc proportionnelle à n^2 lorsque n devient grand.
# @endprof
