from bateau import Bateau


def test_init():
    b1 = Bateau(2, 3)
    assert isinstance(b1, Bateau)
    assert b1.ligne == 2
    assert b1.colonne == 3
    assert b1.longueur == 1
    assert not b1.vertical

    b2 = Bateau(2, 2, longueur=4, vertical=True)
    assert b2.longueur == 4
    assert b2.vertical


def test_positions():
    b1 = Bateau(2, 3, longueur=3)
    assert b1.positions == [(2, 3), (2, 4), (2, 5)]

    b2 = Bateau(2, 3, longueur=3, vertical=True)
    assert b2.positions == [(2, 3), (3, 3), (4, 3)]
