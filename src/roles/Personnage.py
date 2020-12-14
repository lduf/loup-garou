# -*- coding: utf-8 -*-
import discord
from abc import ABC, abstractmethod
class Personnage(ABC):  # Définition de notre classe Personne
    """Classe définissant un personnage caractérisé par :
    - Membre discord
    - Son état de vie (
    mort ou vivant)
    - Son ordre d'appel
    - Les serveurs discords auxquels il appartient
    """

    def __init__(self, membre, role_name, pouvoirs = "", channel_name = ""):
        """Constructeur de notre classe"""
        self.membre = membre
        self.vie = True
        self.role_name = role_name
        self.channel_name = ["Le Village"]
        self.pouvoirs = ["vote"]
        self.ajouter("self.pouvoirs", pouvoirs)
        self.ajouter("self.channel_name", channel_name)


    def ajouter(self, var, content):
        """ Permet d'ajouter le contenu d'une variable à notre objet """

        if (content != ""):
            if (isinstance(content, list)):
                for cont in content:
                    eval(var).append(cont)
            else:
                eval(var).append(content)

    def who(self) :
        descript = "Coucou je suis un {}".format(self.role_name)
        return descript

    def see_channels(self):
        chans = "{}".format(self.channel_name)
        return chans

    def see_pouvoirs(self):
        powers = "{}".format(self.pouvoirs)
        return powers

    @abstractmethod
    def role(self):
        pass
