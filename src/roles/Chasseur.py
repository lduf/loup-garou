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
        pouvoirs = "tuer"
        super(Chasseur, self).__init__(membre, pouvoirs= pouvoirs, role_name="Chasseur")

    def role(self):
        desc = """ Tu es {} \n Tu évolues comme un Villageois classique mais tu as ton petit plus … \n Si tu meurs pendant la partie tu peux utiliser ton fusil !\n
        Tu pourras désigner n'importe quel joueur et tu l'entraineras avec toi dans ta tombe !""".format(self.role_name)
        return desc
