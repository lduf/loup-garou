
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
