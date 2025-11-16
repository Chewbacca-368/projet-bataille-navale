from grille import Grille


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
    print("User story : Plouf dans l'eau !")
    print("Entrez 'exit' pour quitter.")
    grille = Grille(5, 8)
    print(grille)
    print()

    while True:
        try:
            x = input("Entrez la coordonnée x pour tirer (entre 0 et " + str(grille.nb_colonnes - 1) + "): ")
            if x.lower() == 'exit':
                print("Fin de la user story 'Plouf dans l'eau'.")
                break

            y = int(input("Entrez la coordonnée y pour tirer (entre 0 et " + str(grille.nb_lignes - 1) + "): "))

            grille.tirer(y, int(x))
            print(grille)
            print()

        except ValueError:
            print("L'entrée est incorrecte, réessaie.")
        except IndexError:
            print("Coordonnées en dehors de la grille, réessaie.")


if __name__ == "__main__":
    story_grille()
