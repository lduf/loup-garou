import Personnage

class Chasseur(Personnage.Personnage):
    """Classe définissant un Chasseur caractérisé par :
    un Personnage :
        - Membre discord
        - Son état de vie (mort ou vivant)
        - Son ordre d'appel
        - Les serveurs discords auxquels il appartient
        - Nom du role
        - Nom du Channel
    Attribut Personnalisé :

    """

    def __init__(self, membre):
        """Constructeur de notre classe"""
        super(Chasseur, self).__init__(membre, role_name="Chasseur")
