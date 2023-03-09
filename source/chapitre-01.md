# Présentation du problème 

Le problème du sac à dos fait partie des 21 problèmes NP-complets montrés par le mathématicien Richard Karp dans son article « Reducibility Among Combinatorial Problems », publié en 1972.
```{bibliography} references.bib
RICHARD M. KARP, « Reducibility Among Combinatorial Problems », dans Raymond E. Miller et James W. Thatcher, Complexity of Computer Computations, Plenum, 1972, p. 85-103
``` 
Son principe est relativement simple. En effet, la mission consiste à remplir un sac avec une contrainte (comme un volume maximum) ainsi qu’une autre valeur (comme le prix, le poids, etc.) que l’on cherche à optimiser. Pour généraliser, on souhaite obtenir la plus grande valeur possible tout en ne dépassant pas le quota du sac. Dans l’exemple en Figure 1, on souhaite optimiser le prix total des objets ajoutés sans dépasser le poids maximal que peut contenir le sac. 

```{figure} figures/ill_pdsd.jpg
---
width: 50%
align : center
---
Illustration du problème du sac à dos
```

Ce problème concerne de nombreux domaines dans notre société. En cryptographie, il est à l’origine du premier algorithme de chiffrement asymétrique, alors que c’est aussi un problème récurrent dans le domaine financier lorsqu’il s’agit d’élaborer un budget afin de choisir celui qui rapporte le plus. Pour donner un exemple que la plupart d’entre nous avons vécu, il se passe le même phénomène lorsque l’on doit remplir une valise en utilisant le plus de place sans dépasser le poids maximal autorisé par la compagnie aérienne. C’est notamment par ce principe facile à assimiler que ce problème se présente comme l’un des plus populaires du monde informatique. 

Prenons pour exemple un sac possédant un volume maximal. On souhaite y insérer les objets présentant le prix total le plus élevé. Ainsi, il est possible de formuler le problème mathématiquement de cette manière : 

## Formulation mathématique 


```{math}
    Volume\ max. = V \\
    Nbre\ d’objets = n \\ 
    Objet = i\\
    Volume\ de\ l’objet = V_{i} \\
    Prix\ de\ l’objet = P_{i}
```

Exemple de tableau 

| #objet | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| $$P_{i}$$ | 7 | 4 | 3 | 3 |
| $$V_{i}$$ | 13 | 12 | 8 | 10 |

```{math}
    Variable\ X:
    \left\{
        \begin{array}{ll}
            X = 1 \ si \ l’objet\ est\ dans\ le\ sac\\
            X = 0 \ si \ l’objet\ n’est\ pas\ dans\ le\ sac
        \end{array}
    \right.
```

```{math}
    Contrainte\ : 
    \sum_{i=1}^{n} V_{i} < V_{max} \\
    Dans\ l'exemple\ : X_{1}V_{1} + X_{2}V_{2} + X_{3}V_{3} + X_{4}V_{4} \leq V \\
    Tout\ en\ ayant \sum_{i=1}^{n} X_{i}V_{i}\ maximale\\
    
```  

Le problème étant posé, il peut être intéressant de s’attarder sur les différentes méthodes de résolutions du problème. 

## Méthodes de résolution
Il existe ainsi plusieurs méthodes de résolution différentes. Cependant, elles possèdent toutes certains avantages et inconvénients. Il est ici question de les énumérer, de les expliquer ainsi que de souligner leurs points forts et leurs points faibles. 
### Méthode exacte
Il est possible que l’on souhaite obtenir la meilleure solution, que l’on ne puisse pas obtenir mieux. La méthode exacte, ou par la force brute, consiste tout simplement à énumérer de toutes les possibilités d’arrangement, pour sélectionner la meilleure. 

Pour illustrer ce principe, il est possible de raisonner par un arbre de recherche. Il est composé de nœuds, représentés par des cercles, qui représentent l’objet que l’on évalue. Les nœuds situés sur la même ligne correspondent au même objet. On passe à l’objet suivant par des arêtes. Si l’on prend l’objet dans le sac, on indique $$X = 1$$ sur l'arête en question, si l’on ne le prend pas, on lui indique $$X=0$$. Chaque objet possède ainsi 2 flèches qui partent de ce dernier. Lorsque l’on arrive au dernier objet, on calcule la somme des volumes ajoutés ainsi que celle des prix ajoutés, puis on en tire la solution optimale ne dépassant pas la limite de volume. 
```{figure} figures/arbre_rech.jpg
---
width: 50%
align : center
---
Arbre de recherche
```

Sur ce schéma, les feuilles rouges symbolisent que la solution dépasse le quota autorisé et qu’elle n’est donc pas possible, tandis que le nœud bleu indique que la solution est réalisable. On y inscrit la somme des prix des objets. 

Par conséquent, cette méthode permet d’obtenir la meilleure solution, ce qui n’est pas négligeable. Cependant, le développement et les calculs à effectuer augmentent de manière exponentielle lorsque l’on applique ce raisonnement sur un nombre élevé d'objets. Ainsi, la tâche peut prendre un temps effroyable et augmente aussi le risque d’erreurs de calcul si une âme inconsciente se motive à évaluer ce problème à la main. Sur le plan informatique, cette méthode est d’une complexité $$O(n^2)$$ ce qu'il faut éviter. Ainsi, leur longueur les rend souvent moins pertinentes surtout lorsqu’il s’agit de condition à respecter telles que le temps de réponse d’une machine. 

De plus, il peut être utile d’avoir des bornes afin d'optimiser le programme : 

- Borne inférieure : valeur inférieure ou égale à la valeur de la meilleure solution possible. 

- Borne supérieure : valeur maximale, valeur de la meilleure solution réalisable jusqu'à présent.

Ainsi, si les valeurs sont hors bornes, on abandonne la piste. On peut donc aussi changer les bornes si l'on rencontre une valeur minimale ou maximale.

### Méthode approchée/heuristique
La première méthode, dite “approchée” ou “heuristique”, permet d’obtenir une “bonne” solution tout en proposant une certaine économie de temps lors des calculs. Elle consiste en 3 étapes : 

1) Calculer le rapport entre le prix et le volume de chaque objet : $$P_{i} /V_{i}$$ 

2) Trier par ordre décroissant les résultats obtenus. 

3) Sélectionner les objets dans l’ordre du tri et les ajouter tant que le volume maximal n’est pas dépassé. Si un objet ne peut pas être ajouté, passer au prochain jusqu’à atteindre ou se rapprocher au maximum du quota autorisé 

Cette méthode est intéressante car elle apporte un gain de temps conséquent. De plus, elle permet d’avoir une solution acceptable. Enfin, elle semble aisément compréhensible et ne présente que peu de risques d’erreurs de calcul si l’on résout le problème à la main. 

Néanmoins, il est impossible d’utiliser cette démarche lorsque l’on désir obtenir l’arrangement le plus efficace. Pour ajouter à cela, bien qu’il soit possible de l’effectuer quand on ne peut ajouter qu’un seul exemplaire de l’objet, il devient de plus en plus ardu de démarcher de la sorte. 

Sur les nombreux algorithmes basés sur la méthode heuristique, l’algorithme glouton demeure comme l’un des plus populaire. C’est pourquoi je m’attarde sur ce dernier dans le prochain chapitre de ce travail. 