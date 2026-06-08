# Projet 1 – Constellation Interactive (Turtle)


## Description

Dessin de la constellation de Pégase avec le module `turtle` de Python.  
Les étoiles sont stockées dans une liste de tuples et reliées par des lignes.

## Lancer le projet

```bash
python pegase_turtle.py
```

> Nécessite Python 3 (le module `turtle` est inclus par défaut).

## Structure du code

| Élément | Description |
|---|---|
| `etoiles` | Liste de tuples `(x, y, taille, nom)` |
| `connexions` | Liste de tuples `(i, j)` reliant deux étoiles |
| Fond étoilé | 250 points aléatoires avec `random` |
| Boucle lignes | Parcourt `connexions` et trace chaque segment |
| Boucle étoiles | Parcourt `etoiles` et dessine halo + point + étiquette |

## Concepts utilisés

- `turtle.goto(x, y)` — déplacer le crayon
- `turtle.dot(taille)` — dessiner un point
- `turtle.color()` — changer la couleur
- `turtle.write()` — afficher du texte
- `for x, y, taille, nom in etoiles` — décomposition de tuples
- `random.randint()` — positions aléatoires pour le fond

## Les 10 étoiles de Pégase

| Nom | Position |
|---|---|
| dakar | centre |
| thies | haut gauche |
| matam | haut droite |
| fatick | bas centre |
|mbour  | gauche |
| kaolack | loin gauche |
| Saint-lious | droite |
| ziguinchore | loin droite |
| louga | bas gauche |
| lingere | bas droite |


Les étoiles sont reliées par des lignes via la liste `connexions`.
