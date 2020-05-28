# CartographieMeteo ( le programme en lui-même est dans "essaycarte")

# Projet De Cartographie NSI
Projet De CartographieNSI
Présentation Générale:
Ce projet m’a permi de créer une carte de manière accéder à des données météorologiques. 

J’ai voulu répondre à 3 questions:
Quelles stations ont relevé des températures en moyenne plus chaudes que les autres stations? 
Quelles stations ont relevé des temperatures en moyennes plus froides que les autres stations?
Dans une station, quelle a été la température la plus élevée relevée ?
Présentation de la base de donnée publique utilisée:
J’ai utilisé deux bases de données:
L’ une contient les données météorologiques, avec notemment la température (critère auquel il m’était necessaire d’accéder pour répondre à mes questions, bien entendu) 
L’autre contient les coordonées géographiques de chacune des stations météorologiques en France (pas uniquement en métropole, attention)
  

Démarche pour répondre au problème :
Une fois les données trouvées, j’ai commencé par trier mes tables:

Tout d’abord en faisant en sorte de ne garder que les élements qui m’étaient utiles:
Pour la table des données météorologiques, je n’ai gardé que le numéro de la station, ainsi que les températures relevées durant Février, et la date à laquelle ces températures ont été relevées.
Pour la table des coordonnées, j’ai gardé le numéro de station, le nom de station et les coordonnées .

J’ai par la suite crée la map vide.

J’ai ensuite crée une fonction de manière à ajouter un marker pour chacune des sations météorologiques. Cette fonction appelle d’autres fonctions que j’ai crées au fur et à mesure, lorsque j’ai rencontré des problèmes d’affichage notemment :

J’ai donc commencé par créer une fonction qui renvoie un fichier en Json pour pouvoir utiliser Vega- lite et afficher les données de chaque station.
J’ai par la suite crée une fontion qui m’a permis d’afficher la date dans un format que le fichier Json pourrait comprendre .
Il m’a ausssi fallu convertir les températures qui étaient en Kelvin en Celsius. Cela a valu un nouvelle fonction.
Pour finir, j’ai crée deux autres fonctions dans le but de pouvoir faire la moyenne de données . J’ai donc crée une fonction qui extrait uniquement les temperatures dans la table en entrée. J’ai ensuite crée une fonction qui calcule la moyenne des données, et qui appelle pour se faire la fonction qui extrait les températures.  


Le programme en lui même:
Créer une map vide 
Ajoute les markers à l’emplacement de chacune des stations:
Utilise la fonction ajouter markers, qui pour chaque station :
Converti ses données dans le format adéquat,
Créer un fichier Json
Calcule la Moyenne de toutes les données relevées à cette station,
Détermine si cette moyenne  est supérieure ou inférieure à la moyenne des données de  toute les stations, et en fonction de cela détermine la couleur et l’icône qu’aura le marker,
Créer le marker et l’ajoute à la map vide, en utilisant folium, qui va utiliser le fichier json ainsi que la couleur et l’icône du marker préalablement determines. 
Enregistre la map folium dans un fichier HTML
