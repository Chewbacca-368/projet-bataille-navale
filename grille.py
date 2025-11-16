class Grille:

    def __init__(self, lignes=5, colonnes=8):
        self.nb_lignes = lignes
        self.nb_colonnes = colonnes
        self.vide = ' ∿'
        self.touche = 'x'
        self.bateau = '⛵'
        self.matrice = [self.vide] * (lignes * colonnes)

    def _index(self, ligne, colonne):
        return ligne * self.nb_colonnes + colonne

    def tirer(self, ligne, colonne, touche='x'):
        self.touche = touche
        impact = self._index(ligne, colonne)
        self.matrice[impact] = touche

    def __str__(self):
        lignes = []
        for i in range(self.nb_lignes):
            debut = i * self.nb_colonnes
            fin = debut + self.nb_colonnes
            ligne = "".join(self.matrice[debut:fin])
            lignes.append(ligne)
        return "\n".join(lignes)

    def ajoute(self, bateau):
        for ligne, colonne in bateau.positions:
            if not (0 <= ligne < self.nb_lignes and 0 <= colonne < self.nb_colonnes):
                print("Le bateau ne rentre pas dans la grille")
                return

        for ligne, colonne in bateau.positions:
            emplacement = self._index(ligne, colonne)
            self.matrice[emplacement] = bateau.marque
