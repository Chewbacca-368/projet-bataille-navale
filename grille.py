class Grille:

    def __init__(self, lignes=5, colonnes=8):
        self.nb_lignes = lignes
        self.nb_colonnes = colonnes
        self.vide = '∿'
        self.touche = 'x'
        self.matrice = [self.vide] * (lignes * colonnes)

    def _index(self, ligne, colonne):
        return ligne * self.nb_colonnes + colonne

    def tirer(self, ligne, colonne):
        impact = self._index(ligne, colonne)
        self.matrice[impact] = self.touche

    def __str__(self):
        lignes = []
        for i in range(self.nb_lignes):
            debut = i * self.nb_colonnes
            fin = debut + self.nb_colonnes
            ligne = "".join(self.matrice[debut:fin])
            lignes.append(ligne)
        return "\n".join(lignes)
