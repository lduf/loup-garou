# Loup-garou
Projet de création d'un bot de loup garou

## Objectif :

L'objectif est de créé un bot Discord qui gère une partie de Loup Garou. 

## Rôles pris en compte :

Chaque rôles à des caractéristiques spécifiques détaillée ci dessous. Des catégories devraient se dégager, ce qui simplifira le dev en POO.

### Villageois

Un rôle classique puisqu'il ne fait rien mise à part voter la journée.

*Pouvoir :*
 - Vote

### Loup Garou

Ce rôle mène la double vie : il est appelé la nuit et doit tuer les villageois sans se faire repérer par les autres joueurs. 

*Pouvoir :*
 - Vote
 - Tuer la nuit

### Sorcière

Ce role à deux potions (uniquement deux ^^) : une de vie de rappeler qqn a la vie et une potion de mort pour tuer n'importe qui.
Intervient après le vote des loups (donc avant le réveil)

*Pouvoir :*
 - Vote
 - Utiliser ses potions tant qu'elle en a
 
### Voyante

Chaque nuit elle peut voir le rôle d'un autre joueur.

*Pouvoir :*
 - Vote
 - Voir le vote d'un autre joueur
 
### Petite Fille

La petite fille peut voir les loups garous la nuit : comment faire lui donner une liste de noms partiels chaque nuit ou la mettre avec les loups garous sans compter son vote ?

*Pouvoir :*
 - Vote
 - Rester éveillé
 
 
### Chasseur

Un villageois amélioré puisqu'à sa mort il peut tuer un autre joueur.

*Pouvoir :*
 - Vote
 - Tuer un autre joueur à sa mort

### Salvateur

Chaque nuit il désigne une personnne qu'il souhaite sauver. Il ne peut pas sauver deux nuits consécutives la même personne et la protection de la petite ville est inefficace. 

*Pouvoir :*
 - Vote
 - Protection d'un autre joueur


## Schéma de POO

Un schéma semble se dégager des rôles : 

 - une classe personnage semble gérer le tout : 'Membre <Discord>; Pouvoirs [] <Pouvoir>'
 - Une classe par rôle 
