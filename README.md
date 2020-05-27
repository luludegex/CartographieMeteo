# CartographieMeteo ( le programme est dans "essaycarte")

# Projet De Cartographie NSI
Présentation Générale:
Ce projet m’a permi de créer une carte de manière accéder à des données météorologique. 

J’ai voulu répondre à 3 questions:
Quelles stations ont relevés des temperatures en moyenne plus chaudes que les autres stations? 
Quelles stations ont relevé des temperatures moyennes plus froide que les autres stations?
Dans une station, qu’elle a été la temperature la plus élevée relevée ?
Présentation de la base de donnée publique utilisée:
J’ai utilisé deux bases de données:
L’ une contient les données météorologiques, avec notemment la temperature (critère auquel il m’était necessaire d’accéder pour répondre à mes questions, bien entendu) 
L’autre contient les coordonées géographiques de chacune des stations météorologique en France (pas uniquement en metropole, attention)
  

Démarche pour répondre au problème :
Une fois les données trouvées, j’ai commence par trier mes tables:

Tout d’abord en faisant en sorte de ne garder que les élements qui m’étaient utiles:
Pour la tables des données, je n’ai gardé que le numéro de la station, ainsi que les temperatures relevées durant Février, et la date à laquelle ces temperatures avaient été relevées.
Pour la tables des coordonnées, j’ai gardé le numéro de station, le nom de station et les coordonnées .

J’ai par la suite crée la map vide.
J’ai ensuite crée une fonction pour ajouter un marker à chaque sation météorologique.Cette fonction appelle d’autres fonctions que j’ai crées au fur et à mesure, lorsque j’ai rencontré des problèmes d’affichage notemment :
J’ai donc commencé par créer une fonction qui renvoie un fichier en Json pour pouvoir utiliser Vega- lite et afficher les données de chaque station.
J’ai par la suite crée une fontion qui m’a permis d’afficher la date dans un format que le fichier Json pourrait comprendre .
Il m’a ausssi fallu convertir les temperatures qui étaient en Kelvin en Celsius. Cela a valu un nouvelle fonction.
Pour finir, j’ai crée deux autres fonctions dans le but de pouvoir faire la moyennes de données . J’ai donc crée une fonction qui extrait uniquement les temperatures dans la table qu’on lui donne. J’ai ensuite crée une fonction qui calculi la Moyenne des données, et qui appelle pour se faire la function qui extrait les températures.  


Le programme en lui même:
Créer une map vide 
Ajoute les markers à l’emplacement de chacune des stations:
Utilise la fonction ajouter markers, qui pour chaque station :
Converti ses données dans le format adéquat,
Créer un fichier Json
Calcule la Moyenne de toutes les données relevées à cette station,
Détermine si cette moyenne  est supérieur ou inférieur à la Moyenne des données de  toute les stations, et en fonction de cela determine la couleur et l’icone qu’aura le marker,
Créer le marker et l’ajouter à la map vide, en utilisant folium, qui va utiliser le fichier json, la couleur et l’icone du marker préalablement déterminés 
Enregistrer la map folium dans un fichier HTML

