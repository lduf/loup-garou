# -*- coding: utf-8 -*-
import discord
class Personnage:  # Définition de notre classe Personne
    """Classe définissant un personnage caractérisé par :
    - Membre discord
    - Son état de vie (mort ou vivant)
    - Son ordre d'appel
    - Les serveurs discords auxquels il appartient
    """

    def __init__(self, membre, role_name, channel_name = None):
        """Constructeur de notre classe"""
        self.membre = membre
        self.vie = True
        self.role_name = role_name
        self.channel_name = ["Le Village"].append(channel_name)

    def who(self) :
        descript = "Coucou je suis un {} \n".format(self.role_name)
        return descript