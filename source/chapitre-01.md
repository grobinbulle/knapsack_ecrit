# Présentation du problème 

Le problème du sac à dos fait partie des 21 problèmes NP-complets créés par le mathématicien Richard Karp. Son principe est relativement simple. En effet, la mission consiste à remplir un sac avec une contrainte (comme un volume maximum) ainsi qu’une autre valeur (comme le prix, le poids, etc.) que l’on cherche à optimiser. Pour généraliser, on souhaite obtenir la plus grande valeur possible tout en ne dépassant pas le quota du sac. Dans l’exemple en Figure 1, on souhaite optimiser le prix total des objets ajoutés sans dépasser le poids maximal que peut contenir le sac. 

```{figure} figures/ill_pdsd.jpg
---
width: 100%
align : center
---
Illustration du problème du sac à dos
```
Ce problème concerne de nombreux domaines dans notre société. En cryptographie, il est à l’origine du premier algorithme de chiffrement asymétrique alors que c’est aussi un problème récurrence dans le domaine financier lorsqu’il s’agit d’élaborer un budget afin de choisir celui qui rapporte le plus. Pour donner un exemple que la plupart d’entre nous avons vécu, il se passe le même phénomène lorsque l’on doit remplir une valise en utilisant le plus de place sans dépasser le poids maximal autorisé par la compagnie aérienne. C’est notamment par ce principe facile à assimiler que ce problème se présente comme l’un des plus populaire du monde informatique, un univers semblant très complexe pour des non-initiés. 

Prenons pour exemple un sac possédant un volume maximal. On souhaite y insérer les objets présentant le prix total le plus élevé. Ainsi, il est possible de formuler le problème mathématiquement de cette manière : 

## Formulation mathématique 

Volume max. = V 

Nbre d’objets = n 

Objet = i, Volume de l’objet = Vi , Prix de l’objet = Pi 

Exemple de tableau 
```{figure} figures/tableau_sacdos.jpg
---
width: 100%
align : center
---
```
Variable X : 

X = 1 si l’objet est dans le sac 

X = 0 si l’objet n’est pas dans le sac 

Contrainte : Somme des volumes Vi < ou = volume max V 

=> X1V1 + X2V2 + X3V3 + X4V4 < ou = V 

Tout en ayant la somme XiPi maximale. 

Le problème étant posé, il peut être intéressant de s’attarder sur les différentes méthodes de résolutions du problème. 

## Méthodes de résolutions
Il existe ainsi plusieurs méthodes de résolution différentes. Cependant, elles possèdent toutes certains avantages mais aussi certains inconvénients. Il est ici question de les énumérer, les expliquer ainsi que de souligner leurs points forts et leurs points faibles. 
### Méthode exacte
Il est possible que l’on souhaite obtenir la meilleure solution, que l’on ne puisse pas obtenir mieux. La méthode exacte, ou par la force brute, consiste tout simplement à l’énumération de toutes les possibilités d’arrangement, pour en sélectionner la meilleure. 

Pour illustrer ce principe, il est possible de raisonner par un “arbre de recherche”. Il est composé de nœuds, représentés par des cercles, et représentent l’objet que l’on évalue. Les nœuds situés sur la même ligne correspondent au même objet. On passe à l’objet suivant par des flèches. Si l’on prend l’objet dans le sac, on indique X=1 sur celle-ci, si l’on ne le prend pas, on lui indique X=0. Chaque objet possède ainsi 2 flèches qui partent de ce dernier. Lorsque l’on arrive au dernier objet, on calcule la somme des volumes ajoutés ainsi que celle des prix ajoutés, puis on en tire la solution optimale ne dépassant pas la limite de volume. 
```{figure} figures/arbre_rech.jpg
---
width: 100%
align : center
---
Arbre de recherche
```


