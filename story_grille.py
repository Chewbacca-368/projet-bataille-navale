# from grille import Grille

def story_grille():
    """
    User story : "Plouf dans l'eau"
    Utilisateur : un joueur
    Story : On veut pouvoir gérer les tirs de l'adversaire
    Actions :
    1- Créer une grille à 5 lignes et 8 colonnes
    2- Afficher la grille à l'écran
    3- Demande à l'utilisateur de rentrer deux coordonnées x et y
    4- Tirer à l'endroit indiqué sur la grille
    5- Retour en 2
    """

    # grille = Grille(5, 8)

    while True:
        # grille.afficher()

        try:
            x = int(input("Entrez la coordonnée x : "))
            y = int(input("Entrez la coordonnée y : "))

            # grille.tirer(x, y)
            print("Tir effectué en (" + str(x) + "," + str(y) + ")")

        except ValueError:
            print("L'entrée est incorrecte, réessaie.")


if __name__ == "__main__":
    story_grille()
