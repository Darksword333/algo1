#!/usr/bin/python3

# la fonction retourne True si le chat attrape la souris, False sinon
def chat_attrape_souris(carte, saut):
    position_C = [0,0]
    position_s = [0,0]
    presence_C = False
    presence_s = False
    for j in range(len(carte)):
        for i in range(len(carte[0])):
            if carte[j][i] == 'C':
                position_C[1] = i
                position_C[0] = j
                presence_C = True
            if carte[j][i] == 's':
                position_s[1] = i
                position_s[0] = j
                presence_s = True
    ecart = abs(position_s[1] - position_C[1])
    ecart2 = abs(position_s[0] - position_C[0])
    if presence_C == True and presence_s == True:
        if ecart <= abs(saut-ecart2):
            return True
        else :
            return False


# Tests de validation, ne pas modifier !
def test():
    assert chat_attrape_souris(['..C...s..'], 5) 
    assert chat_attrape_souris(['..s...C..'], 5) 
    assert not chat_attrape_souris(['..C...s..'], 2) 
    assert not chat_attrape_souris(['..s...C..'], 2) 
    assert chat_attrape_souris(['..C......', '.........', '....s....'], 5) 
    assert not chat_attrape_souris(['..C......', '.........', '....s....'], 3) 
    assert not chat_attrape_souris(['.C.......', '.........', '......s..'], 5) 
    assert not chat_attrape_souris(['..C......', '.........', '.........'], 5) # miaou !
    assert not chat_attrape_souris(['..s......', '.........', '.........'], 5) # miaou ?

    print("Bien joué !")

test()