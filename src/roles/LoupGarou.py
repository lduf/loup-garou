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
        pouvoirs = ["tuer"]
        super(LoupGarou, self).__init__(membre, role_name="Loup Garou", pouvoirs = pouvoirs, channel_name= channel_name)

    def role(self):
        desc = """ Tu es un {} \n Chaque nuit tu te réveilles avec tes compères. Ensemble vous choississez votre prochaine victime.
        Au réveil du village tu te fondra dans la masse et tu pourras voter comme tous les autres joueurs. À toi de ne pas te faire démasquer !""".format(self.role_name)
        return desc
