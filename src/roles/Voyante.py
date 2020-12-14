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
        pouvoirs = "voir"
        super(Voyante, self).__init__(membre, role_name="Voyante", pouvoirs = pouvoirs, channel_name="Voyante")

    def role(self):
        desc = """ Tu es {} \n Grâce à tes talents de voyance, tu peux voir chaque nuit le rôle d'un des autres joueur. Ce pouvoir est puissant, fait en bon usage !""".format(
            self.role_name)
        return desc