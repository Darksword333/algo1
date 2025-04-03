#!/usr/bin/python3

# la fonction retourne True si le chat attrape la souris, False sinon
def chat_attrape_souris(chaine):
    position_c = 0
    position_s = 0
    for i in range(len(chaine)):
        if chaine[i] == 'C':
            position_c = i
        if chaine[i] == 's':
            position_s = i
    ecart = abs(position_s - position_c)
    if ecart <= 4:
        return True
    else :
        return False
            

# Tests de validation, ne pas modifier !
def test():
    print("Tests chat_attrape_souris...")
    assert not chat_attrape_souris('C....s') 
    assert chat_attrape_souris('C..s') 
    assert not chat_attrape_souris('C.....s') 
    assert chat_attrape_souris('C.s') 
    assert chat_attrape_souris('s...C') 
    assert not chat_attrape_souris('s..........C') 
    print("Bien joué !")

test()