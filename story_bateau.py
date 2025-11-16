from bateau import Bateau


def se_chevauchent(b1, b2):
    for position_1 in b1.positions:
        for position_2 in b2.positions:
            if position_1 == position_2:
                return True
    return False


def story_chevauchement():
    """
    User Story : "Chevauchement"
    Utilisateur : un joueur
    Story : Positionner des bateaux sans chevauchement
    Actions :
    1- Créer un bateau b1
    2- Créer un bateau b2
    3- Vérifier si les deux bateaux se chevauchent
    """
    print("User Story : Chevauchement")

    print("\nCas 1 : Chevauchement")
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 4, longueur=2)
    if se_chevauchent(b1, b2):
        print("Les bateaux se chevauchent. C'est correct.")
    else:
        print("Les bateaux ne se chevauchent pas. Il y a une erreur.")

    print("\nCas 2 : Pas de chevauchement")
    b3 = Bateau(0, 0, longueur=2)
    b4 = Bateau(1, 0, longueur=2)
    if se_chevauchent(b3, b4):
        print("Les bateaux se chevauchent. Il y a une erreur.")
    else:
        print("Les bateaux ne se chevauchent pas. C'est correct.")


if __name__ == "__main__":
    story_chevauchement()
