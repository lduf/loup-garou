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

    def __init__(self, membre, role_name, pouvoirs = [], channel_name = []):
        """Constructeur de notre classe"""
        self.membre = membre
        self.vie = True
        self.role_name = role_name
        self.channel_name = ["Le Village"]
        self.pouvoirs = ["vote"]
        self.channel_name.extend(channel_name)
        self.pouvoirs.extend(pouvoirs)

    def __repr__(self):
        return "{} : {}\n".format(self.membre, self.role_name)

    def who(self) :
        descript = "{} : {}".format(self.membre, self.role_name)
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
