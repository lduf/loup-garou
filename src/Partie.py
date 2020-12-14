# -*- coding: utf-8 -*-
import roles.Villageois
import roles.LoupGarou
import roles.Sorciere
import roles.Voyante
import roles.PetiteFille
import roles.Chasseur
import roles.Salvateur
import random

class Partie():
    def __init__(self, list_joueurs):
        """Constructeur de notre classe Partie"""

        self.joueurs = list_joueurs
        self.roles = self.repartir(len(self.joueurs))
        random.shuffle(self.joueurs) # permet de mélanger la liste de joueurs pour attribuer les rôles aléatoirement
        self.persos = [self.roles[i](self.joueurs[i]) for i in range(len(self.joueurs))] #contient tous les persos pour la partie

        self.persos_vivants = [] #contient la liste des persos encore vivants dans la partie
        self.persos_morts = [] #contient la liste des morts dans la partie
    def repartir(self, nb_joueur):
        if(nb_joueur <= 6):
            print("Erreur : pas assez de joueurs")
        else :
            distrib = [roles.LoupGarou.LoupGarou for _ in range(int(nb_joueur/3))]
            distrib.extend([roles.Voyante.Voyante, roles.Sorciere.Sorciere, roles.PetiteFille.PetiteFille, roles.Salvateur.Salvateur, roles.Chasseur.Chasseur])

            if(len(distrib) < nb_joueur):
                repart_roles = distrib
                repart_roles.extend([roles.Villageois.Villageois for _ in range(nb_joueur-len(repart_roles))])
            else :
                repart_roles = distrib[:nb_joueur]
            return repart_roles
        return None

