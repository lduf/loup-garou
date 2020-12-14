
# -*- coding: utf-8 -*-

import Personnage

class Villageois(Personnage.Personnage):

    """ Classe définissant un Villageois caractérisé par :
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
        super(Villageois, self).__init__(membre, role_name="Villageois")

    def role(self):
        desc = """ Tu es {} \n Tu as un rôle classique. Lorsque le village se réveille, tu votes avec les autres joueurs pour éliminer ceux que tu crois être Loup !""".format(
            self.role_name)
        return desc