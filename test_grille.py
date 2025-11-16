from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert isinstance(g, Grille)
    assert g.nb_lignes == 5
    assert g.nb_colonnes == 8
    assert len(g.matrice) == 5 * 8
    assert all(case == g.vide for case in g.matrice)


def test_tirer():
    g = Grille(5, 8)
    g.tirer(4, 3)
    impact = g._index(4, 3)
    assert g.matrice[impact] == g.touche
