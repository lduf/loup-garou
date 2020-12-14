import Personnage

class Sorciere(Personnage.Personnage):
    """Classe définissant une Sorciere caractérisé par :
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
        pouvoirs= ["empoisonner","reanimer"]
        super(Sorciere, self).__init__(membre, role_name="Sorcière", pouvoirs=pouvoirs, channel_name=["Sorcière"])

    def role(self):
        desc = """ Tu es {} \n Tu as deux potions : une de vie et une de mort. Lorsque vient ton tour, tu pourras décider de sauver la personne tuée par les Loups !
        Tu pourras aussi décider d'empoisoner un autre joueur ! \n Attention tu n'as qu'une potion de chaque !""".format(
            self.role_name)
        return desc