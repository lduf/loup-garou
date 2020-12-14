import sys
import os
sys.path.append(os.path.abspath(os.getcwd()+"/roles"))

import Partie


def main() :
   """ ordre = [roles.Salvateur, roles.Voyante, roles.LoupGarou. roles.Sorciere, roles.Personnage]
    personnages = []
    for _ in range(5):
        personnages.append(roles.Villageois.Villageois("Lucas"))
    for _ in range(2):
        personnages.append(roles.LoupGarou.LoupGarou("Lucas"))

    personnages.append(roles.Sorciere.Sorciere("Lucas"))
    personnages.append(roles.Voyante.Voyante("Lucas"))
    personnages.append(roles.PetiteFille.PetiteFille("Lucas"))
    personnages.append(roles.Chasseur.Chasseur("Lucas"))"""

   """ for perso in personnages:
        print(perso.who())
        print(perso.see_channels())
        print(perso.see_pouvoirs())
        print(perso.role())"""

   joueurs = ["Joueur {}".format(i) for i in range (10)]

   partie = Partie.Partie(joueurs)
   print("{}".format(partie.persos))

if __name__ == "__main__":
   main()
