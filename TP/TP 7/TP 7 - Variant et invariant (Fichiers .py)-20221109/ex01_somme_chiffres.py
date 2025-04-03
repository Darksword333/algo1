def somme_chiffres(n):
    assert n >= 0, "Précondition"
    resultat = 0
    while n > 0:
        v_debut = n
        assert v_debut>0, 'Variant (positif)'
        resultat += n % 10
        n //= 10
        v_apres = n
        assert v_apres<v_debut, 'Variant (decroissant)'
    return resultat


def test_somme_chiffres():
    assert somme_chiffres(1) == 1
    assert somme_chiffres(0) == 0
    assert somme_chiffres(123) == 6
    assert somme_chiffres(123456789) == 45
    print("OK")


test_somme_chiffres()