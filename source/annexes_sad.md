# Annexes
## Annexe 1 - Code de l'algorithme glouton

```python
def knapsack_greedy(weights, values, capacity):
    # Crée une liste de tuples contenant les poids, valeurs et le ratio de chaque objet
    items = list(zip(weights, values))
    # Trie les objets par rapport valeur/poids décroissant
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    max_value = 0
    # Ajoute le premier objet s'il peut tenir dans le sac à dos
    if items[0][0] <= capacity:
        max_value += items[0][1]
        capacity -= items[0][0]
        items = items[1:]
    # Ajoute les autres objets triés par ordre décroissant de rapport valeur/poids jusqu'à atteindre la capacité maximale
    for w, v in items:
        if w <= capacity:
            max_value += v
            capacity -= w
        else:
            break
    return max_value
    # Saisie de l'entrée utilisateur
n = int(input("Entrez le nombre d'objets dans le sac à dos : "))
weights = []
values = []
for i in range(n):
    weights.append(int(input("Entrez le poids entier de l'objet {i+1} : ")))
    values.append(int(input("Entrez la valeur entière de l'objet {i+1} : ")))
capacity = int(input("Entrez la capacité maximale entière du sac à dos : "))

# Résolution du problème du sac à dos
final_value = knapsack_greedy(weights, values, capacity)

# Affichage du résultat
print("La valeur maximale du sac à dos est :", final_value)
```