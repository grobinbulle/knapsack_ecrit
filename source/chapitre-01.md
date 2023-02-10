# Présentation du problème 

Le problème du sac à dos fait partie des 21 problèmes NP-complets créés par le mathématicien Richard Karp. Son principe est relativement simple. En effet, la mission consiste à remplir un sac avec une contrainte (comme un volume maximum) ainsi qu’une autre valeur (comme le prix, le poids, etc.) que l’on cherche à optimiser. Pour généraliser, on souhaite obtenir la plus grande valeur possible tout en ne dépassant pas le quota du sac. Dans l’exemple en Figure 1, on souhaite optimiser le prix total des objets ajoutés sans dépasser le poids maximal que peut contenir le sac. 

```{figure} figures/ill_pdsd.jpg
---
width: 100%
align : center
---
Figure 1. Illustration du problème du sac à dos
```
Ce problème concerne de nombreux domaines dans notre société. En cryptographie, il est à l’origine du premier algorithme de chiffrement asymétrique alors que c’est aussi un problème récurrence dans le domaine financier lorsqu’il s’agit d’élaborer un budget afin de choisir celui qui rapporte le plus. Pour donner un exemple que la plupart d’entre nous avons vécu, il se passe le même phénomène lorsque l’on doit remplir une valise en utilisant le plus de place sans dépasser le poids maximal autorisé par la compagnie aérienne. C’est notamment par ce principe facile à assimiler que ce problème se présente comme l’un des plus populaire du monde informatique, un univers semblant très complexe pour des non-initiés. 

Prenons pour exemple un sac possédant un volume maximal. On souhaite y insérer les objets présentant le prix total le plus élevé. Ainsi, il est possible de formuler le problème mathématiquement de cette manière : 

Formulation mathématique 

Volume max. = V 

Nbre d’objets = n 

Objet = i, Volume de l’objet = Vi , Prix de l’objet = Pi 

Exemple de tableau 


## Titre 1

### Titre 2
