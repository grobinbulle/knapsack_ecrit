# Algorithme Glouton
## Présentation
Comme évoqué dans la section précédente, l’algorithme glouton (ou greedy) appartient à la catégorie des méthodes heuristiques et ne garantit aucunement d’obtenir la bonne réponse. L’algorithme glouton a pour but de choisir la meilleure solution localement. Il procède ici étape par étape. En d’autres termes, si l’on trie les objets par ordre décroissant, l’algorithme contrôle cas après cas si l’objet analysé peut être accepté. Si c’est le cas, l’objet rejoint virtuellement le sac à dos, sinon, il ne le rejoint pas et le programme passe à l’objet suivant. 

Pour illustrer le fonctionnement du programme, il peut être intéressant de s’attarder un exemple concret : Le but est de réaliser le parcours qui, en additionnant les valeurs traversées, nous donne le plus grand résultat total. En réalisant le problème à la main sans algorithme (cf. Figure 1), on réalise qu’il faut d’abord choisir le parcours vert, passant par la case 6, 3, puis 59. 
```{figure} figures/arbre_vert.jpg
---
width: 50%
align : center
---
Chemin choisi manuellement, menant à la réponse optimale 
```
Le programme, quant à lui, prend des décisions localement (cf. Figure 2). Ainsi, lors du choix entre les cases 3 et 7, ce dernier choisira la plus grande valeur, le 7, sans prendre compte de ce qui adviendra derrière. Par conséquent, en empruntant le chemin rouge en appliquant cette logique, la solution optimale n’est pas atteinte. Cependant, le résultat obtenu reste tout de même une solution acceptable étant donné l’économie de mémoire que l’on peut faire si le problème se complexifie. 
```{figure} figures/arbre_rouge.jpg
---
width: 50%
align : center
---
Chemin choisi par l’algorithme glouton, ne menant pas à la réponse optimale  
```
Dans le cadre du problème du sac à dos, il est possible d’appliquer le même raisonnement en triant les objets par ordre décroissant selon leur rapport Pi /Vi, puis regarder si l’on peut rajouter chaque objet en fonction de leur volume et du volume restant dans le sac. 
```{figure} figures/arbre_glouton.jpg
---
width: 70%
align : center
---
Chemin choisi par l’algorithme glouton, ne menant pas à la réponse optimale  
```
Dans l’exemple en figure 3, Il est possible de remarquer que les objets ont été triés dans l’ordre décroissant de leur valeur. L’algorithme ajoute l’objet 1 car son volume (=2) est inférieur au volume restant du sac (=8). Cependant, il ne peut pas accepter l’objet 2 car son volume (=7) est désormais supérieur au volume restant (=8-2=6) et son ajout à l’objet 1 dépasserait la capacité maximale du sac. Néanmoins, il est possible d’ajouter l’objet 3 car son volume (=5) peut être additionné à celui de l’objet 1 sans dépasser le quota (8-(2+5)=1). Ainsi, en additionnant les prix des objets ajoutés est de 33, pour un volume total de 7 ne dépassant pas le quota maximal. Dans cet exemple, il s’agit de la meilleure solution. 
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
Cette implémentation prend trois entrées : poids et valeurs, qui sont des listes des poids et des valeurs des articles, et capacite, qui est le poids maximal que le sac à dos peut contenir. 

L'algorithme commence par créer une liste des indices des articles, triés par ordre décroissant de leur rapport valeur/poids. Cela est fait en utilisant la fonction sorted avec un paramètre key qui spécifie les critères de tri. 

Ensuite, l'algorithme boucle à travers la liste triée des articles et ajoute chaque article au sac à dos s'il ne dépasse pas la capacité. La boucle continue jusqu'à ce que la capacité soit atteinte ou que tous les articles aient été considérés. 

Enfin, l'algorithme renvoie la valeur totale des articles dans le sac à dos. 

Cette implémentation est un algorithme glouton car elle sélectionne les articles dans l'ordre décroissant du rapport valeur/poids, sans tenir compte de l'impact global sur la capacité du sac à dos ou des valeurs et des poids des autres articles qui pourraient être ajoutés plus tard. Cette approche peut produire des solutions sous-optimales, mais elle peut être rapide et simple à mettre en œuvre. 

### Complexité 

La complexité de cet algorithme glouton dépend de la complexité de l'opération de tri et de la boucle qui parcourt la liste triée. 

La fonction sorted a une complexité de temps de O(n log n), où n est le nombre d'éléments à trier. 

Ensuite, la boucle qui parcourt la liste triée a une complexité de temps de O(n), car elle doit parcourir tous les éléments de la liste triée. 

Ainsi, la complexité de temps totale de cet algorithme glouton est O(n log n) pour la fonction de tri et O(n) pour la boucle, soit une complexité totale de O(n log n) pour le pire des cas. 

Il convient de noter que cette complexité de temps ne prend pas en compte le temps nécessaire pour initialiser les listes de poids et de valeurs. La complexité de temps de cette étape dépend de la manière dont les listes sont créées et du nombre d'éléments qu'elles contiennent.
### Analyse du code et compléxité
Ainsi, la complexité de l’algorithme sur une liste d’objet triés est de O(n). Si la liste n’est pas triée, la complexité est alors O(log(n)). 

RESTE A COMPLETER





