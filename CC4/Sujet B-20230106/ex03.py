#!/usr/bin/python3

# FONCTIONS DE BASE
def creer_arbre_vide():
    return None


def creer_arbre(r, g, d):
    return r, g, d


def racine(arbre):
    return arbre[0]


def gauche(arbre):
    return arbre[1]


def droite(arbre):
    return arbre[2]


def est_vide(arbre):
    return arbre == None

# EXERCICE


def diviser_par_deux(arbre):
    if est_vide(arbre):
        return creer_arbre_vide()
    r = racine(arbre)
    g = gauche(arbre)
    d = droite(arbre)
    if r%2 == 0:
        r = r/2
    return creer_arbre(r, diviser_par_deux(g), diviser_par_deux(d))


def test_diviser_par_deux():
    print('Test de la fonction diviser_par_deux')
    assert diviser_par_deux((2, None, None)) == (1, None, None)
    assert diviser_par_deux(creer_arbre_vide()) == creer_arbre_vide()
    arbre1 = (3, None, None)
    assert diviser_par_deux(arbre1) == (3, None, None)

    arbre2 = (4, (5, None, None), (4, None, None))
    # ┌─ 4 ─┐
    # 5     4
    assert diviser_par_deux(arbre2) == (2, (5, None, None), (2, None, None))

    arbre3 = (5, None, (1, None, (5, (8, (9, None, (9, (5, None, None),
              (8, (8, None, None), None))), None), (5, None, None))))
    # 5 ─┐
    #    1 ───────────────────┐
    #                      ┌─ 5 ─┐
    #       ┌───────────── 8     5
    #       9 ────┐
    #          ┌─ 9 ────┐
    #          5     ┌─ 8
    #                8
    assert diviser_par_deux(arbre3) == (5, None, (1, None, (5, (4, (9, None, (
        9, (5, None, None), (4, (4, None, None), None))), None), (5, None, None))))
    print('  OK')


test_diviser_par_deux()
