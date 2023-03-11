# Algorithme Glouton
## Présentation
```{math}
``` 
Comme évoqué dans la section précédente, l’algorithme glouton (ou greedy) appartient à la catégorie des méthodes approchées, ou heuristiques, et ne garantit aucunement d’obtenir la bonne réponse. L’algorithme glouton a pour but de choisir la meilleure solution localement. Il procède ici étape par étape. En d’autres termes, si l’on trie les objets par ordre décroissant, l’algorithme contrôle cas après cas si l’objet analysé peut être accepté. Si c’est le cas, l’objet rejoint définitivement le sac à dos, sinon, il ne le rejoint pas et le programme passe à l’objet suivant. 

Pour illustrer le fonctionnement du programme, il peut être intéressant de s’attarder un exemple concret, plus simplifié que le sac à dos : le but est de réaliser le parcours qui, en additionnant les valeurs traversées, nous donne la plus grande somme totale, tout cela sans aucune contrainte ou quota. En réalisant le problème à la main sans algorithme (cf. Figure 3), on réalise qu’il faut d’abord choisir le parcours vert, passant par le nœud 6, 3, puis 59. 

```{warning}
Il est important de noter que chaque nœud des exemples en figure 3 et 4 représente un objet différent : l'objet du nœud 3 n'est pas le même que l'objet du nœud 7. Dans le problème du sac à dos (cf. figure 5), au contraire, les nœuds d'une même ligne représentent le même objet.
```

```{figure} figures/arbre_vert.jpg
---
width: 50%
align : center
---
Chemin choisi manuellement, menant à la réponse optimale 
```
Le programme, quant à lui, prend des décisions localement (cf. Figure 4). Ainsi, lors du choix entre les nœuds 3 et 7, ce dernier choisira la plus grande valeur, le 7, sans tenir compte de ce qui adviendra par la suite. Par conséquent, en empruntant le chemin rouge en appliquant cette logique, la solution optimale n’est pas atteinte. Cependant, le résultat obtenu reste tout de même une solution acceptable étant donné l’économie de temps que l’on peut faire par rapport à la méthode "force brute" si le problème se complexifie par l'ajout de plusieurs objets. 
```{figure} figures/arbre_rouge.jpg
---
width: 50%
align : center
---
Chemin choisi par l’algorithme glouton, ne menant pas à la réponse optimale  
```

Dans le cadre du problème du sac à dos, il est possible d’appliquer le même raisonnement en triant les objets par ordre décroissant selon leur rapport prix/volume de chaque objet afin d'intégrer les objets les plus intéressants en premier. Après cela, on regarde si l’on peut rajouter chaque objet en fonction de son volume et du volume restant dans le sac. 
```{figure} figures/arbre_glouton.jpg
---
width: 70%
align : center
---
Chemin choisi par l’algorithme glouton  
```
Représentation des objets sous forme de tableau :
| #objet | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Prix | 23 | 21 | 10 |
| Poids | 2 | 7 | 5 |
| Rapport prix/poids | 11.5 | 3 | 2 |
Dans l’exemple en figure 3, l’algorithme ajoute l’objet 1 car son volume $$V_{i} = 2$$ est inférieur au volume restant du sac. $$V=8$$ Cependant, il ne peut pas accepter l’objet 2 car son volume $$V_{i} = 7$$ est désormais supérieur au volume restant $$V =8-2=6$$ et son ajout à l’objet 1 dépasserait la capacité maximale du sac. Néanmoins, il est possible d’ajouter l’objet 3 car son volume $$V_{i} = 5$$ peut être additionné à celui de l’objet 1 sans dépasser le quota $$V = (8-(2+5)=1)$$ Ainsi, $$P = \sum_{i=1}^{n} Prix_{i} = 33$$ pour un volume total$$V = \sum_{i=1}^{n} V_{i} = 7$$  ne dépassant pas le quota maximal. Dans cet exemple, il s’agit de la meilleure solution. 
##  Résolution du problème par l’algorithme glouton 
Le problème peut ainsi être résolu par le code python ci-dessous :

```python 
def algo_glouton(poids, valeurs, capacite): 
    items = sorted(range(len(poids)), key=lambda i: -valeurs[i] / poids[i]) 
    poids_total = 0 
    valeur_totale = 0 
    for i in items: 
        if poids_total + poids[i] <= capacite: 
            poids_total += poids[i] 
            valeur_totale += valeurs[i] 
    return valeur_totale
```
Cette implémentation prend trois entrées : `poids` et `valeurs`, qui sont des listes des poids et des valeurs des articles, et `capacite`, qui est le poids maximal que le sac à dos peut contenir. 

L'algorithme commence par créer une liste des indices des différents articles, triés par ordre décroissant de leur rapport valeur/poids. Cela est fait en utilisant la fonction `sorted` avec un paramètre `key` qui spécifie les critères de tri. 

Ensuite, l'algorithme boucle à travers la liste triée des articles et ajoute chaque article au sac à dos s'il ne dépasse pas la capacité. La boucle continue jusqu'à ce que la capacité soit atteinte ou que tous les articles aient été considérés. 

Enfin, l'algorithme renvoie la valeur totale des articles dans le sac à dos. 

Cette implémentation est un algorithme glouton car elle sélectionne les articles dans l'ordre décroissant du rapport valeur/poids, sans tenir compte de l'impact global sur la capacité du sac à dos ou des valeurs et des poids des autres articles qui pourraient être ajoutés plus tard. Cette approche peut produire des solutions sous-optimales, mais elle est rapide et simple à mettre en œuvre. 

### Complexité 

La complexité de cet algorithme glouton dépend de la complexité de l'opération de tri et de la boucle qui parcourt la liste triée. 

La fonction `sorted` a une complexité de temps de $$O(n log(n))\ , \ n = nombre \ élément \ à \ trier$$

Ensuite, la boucle qui parcourt la liste triée a une complexité de temps de $$O(n)$$ car elle doit parcourir tous les éléments de la liste triée. 

La complexité de temps totale de cet algorithme glouton est $$O(n log(n))$$ pour la fonction de tri et $$O(n)$$ pour la boucle, soit une complexité totale de $$O(n log (n))$$

Ainsi, l'algorithme glouton est plus rapide que l'algorithme par la force brute pour un nombre important d'objets. Néanmoins, pour un problème contenant peu d'objets, il se peut que la méthode gloutonne soit plus lente en raison de la complexité du tri initial des objets en fonction de leur rapport valeur/poids. 

Dans un autre registre, si l'on souhaite améliorer cette méthode afin de trouver une meilleure solution, il peut être intéressant de s'attarder sur un algorithme glouton récursif capable de revenir en arrière pour explorer les diverses branches. Dans le pire des cas, la complexité de cet algorithme est exponentielle, c'est-à-dire qu'elle dépend de la taille de l'entrée et augmente rapidement avec le nombre d'objets à considérer. Cette complexité est due au fait que, dans certains cas, l'algorithme peut prendre une mauvaise décision à un moment donné, ce qui le conduit à explorer une branche de l'arbre de recherche qui ne contient pas la solution optimale. En conséquence, l'algorithme peut potentiellement examiner toutes les combinaisons possibles d'objets à placer dans le sac, ce qui donne une complexité exponentielle $$ O(2^{n})$$.

## Autres méthodes approchées
L'algorithme glouton n'est pas l'unique méthode approchée. En effet, si l'on s'attarde sur les autres manières approchées de résoudre le problème, on peut évoquer les algorithmes génitiques et ceux basés sur les colonies de fourmies.
### Algorithme génétique
L'algorithme génétique est une méthode d'optimisation qui simule le processus de sélection naturelle pour résoudre des problèmes d'optimisation. Il est souvent utilisé pour résoudre des problèmes d'optimisation combinatoire, tels que le problème du sac à dos.

Il fonctionne de la manière suivante :

1) Génération de la population initiale : On crée une population de solutions candidates. Chaque solution représente une sélection d'objets à potentiellement inclure dans le sac à dos. 

2) Tri des solutions : On évalue chaque solution de la population en calculant la valeur totale des objets qu'elle contient et en vérifiant si elle respecte la limite de poids du sac à dos. Après cela, on sélectionne les meilleures solutions pour la prochaine génération de solution

3) Combination : On combine certaines parties des solutions sélectionnées pour créer de nouvelles solutions candidates, constituant une nouvelle génération.

4) Mutation : On applique une mutation, consistant en un échange de deux objets ou en l'ajout ou la suppression d'un objet, à certaines solutions de la population pour ajouter de la diversité. 

5) Évaluation des solutions : On évalue les nouvelles solutions de la population.

6) Répétition : On répète les étapes 3 à 5 jusqu'à ce qu'une condition d'arrêt, telle qu'un nombre maximal d'itération ou un temps maximal, soit atteinte. On retourne ensuite la meilleure solution obtenue.

### Algorithme basé sur les colonies de fourmies

L'algorithme basé sur les colonies de fourmis est une technique d'optimisation heuristique inspirée du comportement des fourmis. Cette méthode peut être appliquée pour résoudre des problèmes d'optimisation combinatoire tels que le problème du sac à dos.

L'algorithme basé sur les colonies de fourmis pour le problème du sac à dos fonctionne de la manière suivante :

1) Initialisation : On commence par générer une population de fourmis artificielles, qui représentent les "constructeurs" des solutions candidates. Chaque fourmi commence avec une solution vide et se déplace dans l'espace des solutions pour créer une solution candidate selon une règle de transition stochastique. Cette règle permet à la fourmi de choisir un objet à ajouter à la solution en fonction de sa valeur et de son poids. Les objets les plus rentables ont une probabilité plus élevée d'être choisis, mais les objets plus lourds ont une probabilité plus faible.

2) Évaluation de la solution : Une fois que la fourmi a ajouté un objet à sa solution, celle-ci est évaluée pour voir si elle respecte la limite de poids du sac à dos. Si la limite est dépassée, la solution est invalide.

3) Mise à jour de la phéromone : Après que toutes les fourmis ont construit leur solution, la phéromone est mise à jour. Les fourmis déposent une quantité de phéromone proportionnelle à la qualité de leur solution. Les solutions de haute qualité reçoivent plus de phéromone.

4) Évaporation de la phéromone : La phéromone déposée par les fourmis s'évapore avec le temps, de sorte que les pistes phéromonales les plus anciennes, et donc meilleures, soient progressivement éliminées.

5) Condition d'arrêt : L'algorithme s'arrête lorsque les conditions d'arrêt prédéfinies sont atteintes, telles que le nombre maximal d'itérations ou un temps de calcul maximal.

6) Récupération de la meilleure solution : La meilleure solution trouvée est retournée comme solution finale du problème.
```{figure} figures/antfrance.jpg
---
width: 50%
align : center
---
Illustration d'un algorithme de colonies de fourmis cherchant à trouver le plus court chemin entre des villes françaises dans le cadre du problème du voyageur. TECHNO SCIENCE.NET
```