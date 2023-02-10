# Algorithme Glouton
## Présentation
Comme évoqué dans la section précédente, l’algorithme glouton (ou greedy) appartient à la catégorie des méthodes heuristiques et ne garantit aucunement d’obtenir la bonne réponse. L’algorithme glouton a pour but de choisir la meilleure solution localement. Il procède ici étape par étape. En d’autres termes, si l’on trie les objets par ordre décroissant, l’algorithme contrôle cas après cas si l’objet analysé peut être accepté. Si c’est le cas, l’objet rejoint virtuellement le sac à dos, sinon, il ne le rejoint pas et le programme passe à l’objet suivant. 

Pour illustrer le fonctionnement du programme, il peut être intéressant de s’attarder un exemple concret : Le but est de réaliser le parcours qui, en additionnant les valeurs traversées, nous donne le plus grand résultat total. En réalisant le problème à la main sans algorithme (cf. Figure 1), on réalise qu’il faut d’abord choisir le parcours vert, passant par la case 6, 3, puis 59. 
```{figure} figures/arbre_vert.jpg
---
width: 100%
align : center
---
Chemin choisi manuellement, menant à la réponse optimale 
```
Le programme, quant à lui, prend des décisions localement (cf. Figure 2). Ainsi, lors du choix entre les cases 3 et 7, ce dernier choisira la plus grande valeur, le 7, sans prendre compte de ce qui adviendra derrière. Par conséquent, en empruntant le chemin rouge en appliquant cette logique, la solution optimale n’est pas atteinte. Cependant, le résultat obtenu reste tout de même une solution acceptable étant donné l’économie de mémoire que l’on peut faire si le problème se complexifie. 
```{figure} figures/arbre_rouge.jpg
---
width: 100%
align : center
---
Chemin choisi par l’algorithme glouton, ne menant pas à la réponse optimale  
```
Dans le cadre du problème du sac à dos, il est possible d’appliquer le même raisonnement en triant les objets par ordre décroissant selon leur rapport Pi /Vi, puis regarder si l’on peut rajouter chaque objet en fonction de leur volume et du volume restant dans le sac. 
```{figure} figures/arbre_glouton.jpg
---
width: 100%
align : center
---
Chemin choisi par l’algorithme glouton, ne menant pas à la réponse optimale  
```
Dans l’exemple en figure 3, Il est possible de remarquer que les objets ont été triés dans l’ordre décroissant de leur valeur. L’algorithme ajoute l’objet 1 car son volume (=2) est inférieur au volume restant du sac (=8). Cependant, il ne peut pas accepter l’objet 2 car son volume (=7) est désormais supérieur au volume restant (=8-2=6) et son ajout à l’objet 1 dépasserait la capacité maximale du sac. Néanmoins, il est possible d’ajouter l’objet 3 car son volume (=5) peut être additionné à celui de l’objet 1 sans dépasser le quota (8-(2+5)=1). Ainsi, en additionnant les prix des objets ajoutés est de 33, pour un volume total de 7 ne dépassant pas le quota maximal. Dans cet exemple, il s’agit de la meilleure solution. 
##  Résolution du problème par l’algorithme glouton 
Le problème peut ainsi être résolu par le code python ci-dessous
`````{admonition} Code Markdown
````markdown
```python 
for i = 1 to n  
   do x[i] = 0  
weight = 0  
for i = 1 to n  
   if weight + w[i] ≤ W then   
      x[i] = 1  
      weight = weight + w[i]  
   else  
      x[i] = (W - weight) / w[i]  
      weight = W  
      break  
return x 
```
````
`````
### Analyse du code et compléxité
Ainsi, la complexité de l’algorithme sur une liste d’objet triés est de O(n). Si la liste n’est pas triée, la complexité est alors O(log(n)). 

RESTE A COMPLETER





