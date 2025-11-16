class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        emplacements = []
        for i in range(self.longueur):
            if self.vertical:
                emplacements.append((self.ligne + i, self.colonne))
            else:
                emplacements.append((self.ligne, self.colonne + i))
        return emplacements
