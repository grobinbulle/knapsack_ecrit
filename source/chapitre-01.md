# Présentation du problème 

Le problème du sac à dos fait partie des 21 problèmes NP-complets montrés par le mathématicien Richard Karp dans son article « Reducibility Among Combinatorial Problems », publié en 1972.
```{bibliography} references.bib
RICHARD M. KARP, « Reducibility Among Combinatorial Problems », dans Raymond E. Miller et James W. Thatcher, Complexity of Computer Computations, Plenum, 1972, p. 85-103
``` 
Son principe est relativement simple. En effet, la mission consiste à remplir un sac avec une contrainte (comme un volume maximum) ainsi qu’une autre valeur (comme le prix, le poids, etc.) que l’on cherche à optimiser. Pour généraliser, on souhaite obtenir la plus grande valeur possible tout en ne dépassant pas le quota du sac. Dans l’exemple en Figure 2.1, on souhaite optimiser le prix total des objets ajoutés sans dépasser le poids maximal que peut contenir le sac. 

```{figure} figures/ill_pdsd.jpg
---
width: 50%
align : center
---
Illustration du problème du sac à dos, COMPLEX SYSTEMS AI
```

Ce problème concerne de nombreux domaines dans notre société. En cryptographie, il est à l’origine du premier algorithme de chiffrement asymétrique, alors que c’est aussi un problème récurrent dans le domaine financier lorsqu’il s’agit d’élaborer un budget afin de choisir celui qui rapporte le plus. Pour donner un exemple que la plupart d’entre nous avons vécu, il se passe le même phénomène lorsque l’on doit remplir une valise en utilisant le plus de place sans dépasser le poids maximal autorisé par la compagnie aérienne. C’est notamment par ce principe facile à assimiler que ce problème se présente comme l’un des plus populaires du monde informatique. 

Prenons pour exemple un sac possédant un volume maximal. On souhaite y insérer les objets présentant le prix total le plus élevé. Ainsi, il est possible de formuler le problème mathématiquement de cette manière : 

## Formulation mathématique 

Exemple de tableau 

| #objet | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Pi | 7 | 4 | 3 | 3 |
| Vi | 13 | 12 | 8 | 10 |


```{math}
    Volume\ max. = V \\
    Nbre\ d’objets = n \\ 
    Objet = i\\
    Volume\ de\ l’objet = V_{i} \\
    Prix\ de\ l’objet = P_{i}
```

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

Pour illustrer ce principe, il est possible de raisonner par un arbre de recherche. Il est composé de nœuds, représentés par des cercles, qui représentent l’objet que l’on évalue. Les nœuds situés sur la même ligne correspondent au même objet. On passe à l’objet suivant par des arêtes. Si l’on prend l’objet dans le sac, on indique 
```{math}
    X = 1
```
sur l'arête en question, si l’on ne le prend pas, on lui indique 
```{math}
    X = 0
```
Chaque objet possède ainsi 2 flèches qui partent de ce dernier. Lorsque l’on arrive au dernier objet, on calcule la somme des volumes ajoutés ainsi que celle des prix ajoutés, puis on en tire la solution optimale ne dépassant pas la limite de volume. 
```{figure} figures/arbre_rech.jpg
---
width: 50%
align : center
---
Arbre de recherche, INTERSTICES.INFO
```

Sur ce schéma, les nœuds rouges symbolisent que la solution dépasse le quota autorisé et qu’elle n’est donc pas possible, tandis que le nœud bleu indique que la solution est réalisable. On y inscrit la somme des prix des objets. 

Par conséquent, cette méthode permet d’obtenir la meilleure solution, ce qui n’est pas négligeable. Cependant, le développement et les calculs à effectuer augmentent de manière exponentielle lorsque l’on applique ce raisonnement sur un nombre élevé d'objets. Ainsi, la tâche peut prendre un temps effroyable et augmente aussi le risque d’erreurs de calcul si une âme inconsciente se motive à évaluer ce problème à la main. Ainsi, leur longueur les rend souvent moins pertinentes surtout lorsqu’il s’agit de condition à respecter telles que le temps de réponse d’une machine. 

Cette méthode explore ainsi
```{math}
    2^{n}
```
chemins différents. Ainsi, si l'on s'intéresse à problème contenant 10 objets, on aura 
```{math}
    2^{10} = 1'024 \ combinaisons
```
Pour un problème de 20 objets, on aura 
```{math}
    2^{20} = 1'048'576 \ combinaisons
```
Le nombre de combinaisons augmente ainsi exponentiellement. Il semble dès lors évident que cette méthode prend énormement de temps si l'on s'intéresse à de nombreux objets.

Il peut être intéressant de s'appuyer sur le branch and bound afin de simplifier la recherche. En effet, son principe consiste en la subdivision de l'arbre puis en l'évaluation de la meilleure solution comprise dans la section étudiée. Seule cette dernière est stockée jusqu'à ce que l'on trouve une solution plus optimale, les autres sont directement éliminées. Cette méthode est donc pratique pour les problèmes de tailles conséquentes et permet tout de même d'atteindre la solution optimale. De plus, il n'y a donc pas besoin de stocker chaque méthode en mémoire, ce qui permet d'importantes économies. Là où la complexité de la méthode par la force brute atteint
```{math}
    O(2^{n})
```
Le branch and bound permet de réduire considérablement le temps de calcul et d'obtenir des solutions plus rapidement. Bien que la complexité de cette dernière méthode soit également exponentielle dans le pire des cas, elle est généralement beaucoup plus faible que celle de la méthode par force brute.
### Méthodes approchées 
Les méthodes approchées (ou heuristiques) permettent de trouver de manière rapide une solution réalisable à un problème. Cependant, cette solution n’est pas forcément la solution optimale.
L’objectif d’une méthode heuristique est donc de trouver une solution la plus proche possible de celle d’une
méthode exacte tout en étant plus rapide. Plus le résultat obtenu est proche de la solution optimale,
meilleure est l’heuristique.

Sur les nombreux algorithmes basés sur la méthode approchée, l’algorithme glouton demeure comme l’un des plus populaire. C’est pourquoi je m’attarde sur ce dernier dans le prochain chapitre de ce travail. 