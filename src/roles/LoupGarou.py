import Personnage

class LoupGarou(Personnage.Personnage):
    """Classe définissant un Loup Garou caractérisé par :
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
        channel_name = ["Loup Garou"]
        super(LoupGarou, self).__init__(membre, role_name="Loup Garou", channel_name= channel_name)
