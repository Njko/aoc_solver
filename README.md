# Advent of Code Solver

Ce projet est un ensemble de solutions pour les défis de [Advent of Code](https://adventofcode.com/). Il est structuré pour permettre de résoudre les défis de manière organisée et de documenter les solutions.

## Qu'est-ce que l'Advent of Code ?

L'Advent of Code est un calendrier de l'Avent de petits puzzles de programmation qui peuvent être résolus dans n'importe quel langage de programmation. Les gens utilisent ces défis pour se préparer à des entretiens techniques, s'entraîner à la programmation, apprendre de nouveaux langages, ou simplement pour s'amuser.

## Structure du projet

Le projet est organisé de la manière suivante :

- `solvers/` : Contient le code source pour résoudre les défis.
  - `days/` : Les solutions sont organisées par année et par jour.
    - `yXXXX/` : Contient les solutions pour l'année XXXX.
      - `day_DD.py` : Solution pour le jour DD.
  - `solver.py` : Définit la classe de base abstraite pour tous les solveurs. Chaque solveur de jour doit hériter de cette classe et implémenter les méthodes `part1` et `part2`.
  - `main.py` : Le point d'entrée principal pour exécuter les solveurs.
- `doc/` : Contient la documentation et les explications des solutions.
  - `walkthrough/` : Des explications détaillées pour chaque jour.

## Comment l'utiliser

Pour exécuter la solution pour un jour spécifique, vous pouvez utiliser la commande suivante :

```bash
python -m solvers.main <année> <jour>
```

Par exemple, pour exécuter la solution du jour 1 de l'année 2015 :

```bash
python -m solvers.main 2015 1
```

Le script récupérera automatiquement les données d'entrée du site de l'Advent of Code et les mettra en cache localement.
