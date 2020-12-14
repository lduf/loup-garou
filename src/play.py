import sys
import os
sys.path.append(os.path.abspath(os.getcwd()+"/roles"))

import roles.Villageois
import roles.LoupGarou
import roles.Sorciere
import roles.Voyante
import roles.PetiteFille
import roles.Chasseur



def main() :

    personnages = []
    for _ in range(5):
        personnages.append(roles.Villageois.Villageois("Lucas"))
    for _ in range(2):
        personnages.append(roles.LoupGarou.LoupGarou("Lucas"))

    personnages.append(roles.Sorciere.Sorciere("Lucas"))
    personnages.append(roles.Voyante.Voyante("Lucas"))
    personnages.append(roles.PetiteFille.PetiteFille("Lucas"))
    personnages.append(roles.Chasseur.Chasseur("Lucas"))

    for perso in personnages:
        print(perso.who())

if __name__ == "__main__":
   main()
