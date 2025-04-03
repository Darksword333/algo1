#!/usr/bin/python3


def maximum_parcours(carte, position, chemin):
    ...

#validation, ne pas modifier !
def test():
    assert maximum_parcours([[1,0,0],[3,0,4],[2,0,1]], (2,1), ['NO','NE','SE','SO']) == 4
    assert maximum_parcours([[1,3,9],[3,9,4],[9,0,1]], (2,1), ['NO','NE','SE','SO']) == 4
    assert maximum_parcours([[1,1,1],[1,1,1],[1,1,1]], (2,1), ['NO','NE','SE','SO']) == 1
    print("  OK !")

test()

