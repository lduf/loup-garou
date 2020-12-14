import Personnage

class PetiteFille(Personnage.Personnage):
    """Classe définissant une PetiteFille caractérisé par :
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
        pouvoirs = "espionner"
        super(PetiteFille, self).__init__(membre, role_name="Petite Fille", pouvoirs = pouvoirs, channel_name="Petite Fille")

    def role(self):
        desc = """ Tu es {} \n Tu évolues comme un Villageois classique mais tu as ton petit plus … \n Tu n'arrives pas à dormir la nuit et tu regardes par la fenêtre. \n 
        Tu verras alors des choses pendant la nuit ! Tu verras peut être l'identité des Loups mais aussi celle de la voyante, sorcière ou des autres ! À toi de garder l'oeil ouvert !""".format(
            self.role_name)
        return desc