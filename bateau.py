class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False, marque=None):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque

    @property
    def positions(self):
        emplacements = []
        for i in range(self.longueur):
            if self.vertical:
                emplacements.append((self.ligne + i, self.colonne))
            else:
                emplacements.append((self.ligne, self.colonne + i))
        return emplacements

    def coule(self, grille):
        for (l, c) in self.positions:
            index = grille._index(l, c)
            if grille.matrice[index] != grille.touche:
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque="🚢")


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque="⛴️")


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🚣")


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🐟")
