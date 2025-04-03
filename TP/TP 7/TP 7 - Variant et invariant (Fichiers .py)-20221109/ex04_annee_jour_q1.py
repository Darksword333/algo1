def est_bissextile(annee):
  return annee%4==0 and annee%100!=0 or annee%400==0

def nb_jours_annee(annee):
    if est_bissextile(annee):
        return 366
    else:
        return 365

def calculer_annee_jour(jours):
    annee = 1980
    while jours>nb_jours_annee(annee):
        v_debut = jours
        assert v_debut>0, 'Variant positif'
        if jours > nb_jours_annee(annee):
            jours -= nb_jours_annee(annee)
            annee += 1
        v_fin = jours
        assert v_fin<=v_debut, 'Variant décroissant'
    return annee,jours
'''def calculer_annee_jour(jours):
  annee = 1980
  while jours>365:
    v_debut = jours
    assert v_debut>0,'Variant'
    if est_bissextile(annee):
      if jours > 366:
        jours -= 366
        annee += 1
    else:
      jours -= 365
      annee += 1
    v_fin = jours
    assert v_fin<=v_debut,'Variant'
  return annee,jours
'''
def test_calculer_annee_jour():
  print('Test de la fonction calculer_annee_jour')
  assert calculer_annee_jour(1)==(1980,1)
  assert calculer_annee_jour(365)==(1980,365)
  assert calculer_annee_jour(367)==(1981,1)
  assert calculer_annee_jour(380)==(1981,14)
  assert calculer_annee_jour(10592)==(2008,365)
  assert calculer_annee_jour(10594)==(2009,1)
  print('  pas vraiment OK...')
  assert calculer_annee_jour(10593)==(2008,366)
  assert calculer_annee_jour(366)==(1980,366)
  print('  OK')

test_calculer_annee_jour()

'''
1)a) il semblerait que cela boucle a l infini
c) comme cela vaut 366 jours cela boucle a l infini car on rentre nulle part'''