import Personnage

class Salvateur(Personnage.Personnage):
    """Classe définissant une Salvateur caractérisé par :
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
        super(Salvateur, self).__init__(membre, role_name="Salvateur", channel_name=["Salvateur"])