import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


def placer_bateaux_aleatoirement(grille, bateau):
    positions_possibles = []

    for vertical in [False, True]:
        max_ligne = grille.nb_lignes - (bateau.longueur if vertical else 1)
        max_col = grille.nb_colonnes - (bateau.longueur if not vertical else 1)

        for ligne in range(max_ligne + 1):
            for col in range(max_col + 1):
                temp = type(bateau)(ligne, col, vertical=vertical)
                chevauchement = False
                for (l, c) in temp.positions:
                    index = grille._index(l, c)
                    if grille.matrice[index] != grille.vide:
                        chevauchement = True
                        break
                if not chevauchement:
                    positions_possibles.append((ligne, col, vertical))

    ligne, col, vertical = random.choice(positions_possibles)
    bateau.ligne = ligne
    bateau.colonne = col
    bateau.vertical = vertical
    grille.ajoute(bateau)


def main():
    g = Grille(8, 10)
    flotte = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]

    for bateau in flotte:
        placer_bateaux_aleatoirement(g, bateau)

    print("Bienvenue dans le jeu de la bataille navale !")
    print("Voici la grille avec la flotte de bauteaux placée aléatoirement :")
    print(g)

    # Demande à l'utilisateur de tirer
    # Affiche la grille après le tir
    # Continue jusqu'à ce que tous les bateaux soient coulés


if __name__ == "__main__":
    main()
