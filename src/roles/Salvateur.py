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
        pouvoirs = "sauver"
        super(Salvateur, self).__init__(membre, role_name="Salvateur", pouvoirs = pouvoirs, channel_name="Salvateur")

    def role(self):
        desc = """ Tu es {} \n Tu es le gentil de la bande. \n Chaque nuit tu te réveilles et grâce à tes pouvoirs tu peux sauver une personne des griffes des Loups.
        Attention tu ne peux pas protéger la même personne deux nuits de suite et ta protection est inefficace sur la petite fille !""".format(
            self.role_name)
        return desc