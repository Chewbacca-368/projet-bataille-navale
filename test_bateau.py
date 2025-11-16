from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille


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


def test_coule():
    g = Grille(5, 5)
    b1 = Bateau(1, 1, longueur=2)

    g.ajoute(b1)
    assert not b1.coule(g)

    g.tirer(1, 1)
    assert not b1.coule(g)

    g.tirer(1, 2)
    assert b1.coule(g)


def test_porte_avion():
    g = Grille(5, 5)
    b = PorteAvion(1, 1)
    assert b.longueur == 4
    assert b.marque == "🚢"
    assert not b.vertical
    assert b.positions == [(1, 1), (1, 2), (1, 3), (1, 4)]

    g.ajoute(b)
    for (l, c) in b.positions:
        assert g.matrice[g._index(l, c)] == "🚢"


def test_croiseur():
    g = Grille(5, 5)
    b = Croiseur(2, 2, vertical=True)
    assert b.longueur == 3
    assert b.marque == "⛴️ "
    assert b.vertical
    assert b.positions == [(2, 2), (3, 2), (4, 2)]

    g.ajoute(b)
    for (l, c) in b.positions:
        assert g.matrice[g._index(l, c)] == "⛴️ "


def test_torpilleur():
    g = Grille(5, 5)
    b = Torpilleur(3, 3, vertical=True)
    assert b.longueur == 2
    assert b.marque == "🚣"
    assert b.positions == [(3, 3), (4, 3)]

    g.ajoute(b)
    for (l, c) in b.positions:
        assert g.matrice[g._index(l, c)] == "🚣"


def test_sous_marin():
    g = Grille(5, 5)
    b = SousMarin(3, 3)
    assert b.longueur == 2
    assert b.marque == "🐟"
    assert b.positions == [(3, 3), (3, 4)]

    g.ajoute(b)
    for (l, c) in b.positions:
        assert g.matrice[g._index(l, c)] == "🐟"
