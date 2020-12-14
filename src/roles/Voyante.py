import Personnage

class Voyante(Personnage.Personnage):
    """Classe définissant une Voyante caractérisé par :
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
        super(Voyante, self).__init__(membre, role_name="Voyante", channel_name=["Voyante"])