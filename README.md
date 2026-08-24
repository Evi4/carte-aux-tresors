# La carte aux trésors

Guidez les aventuriers en quête de trésors en simulant des déplacements et la collecte de trésors.

## Prérequis

- [uv](https://docs.astral.sh/uv/) installé sur la machine

## Installation

```
# Installer uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Installer Python 3.13 pour le projet
uv python install 3.13
```

## Lancer le programme

```
uv run python src/carte_aux_tresors/main.py --input <chemin_fichier_entree> --output <chemin_fichier_sortie>
```

Exemple avec le fichier d'exemple :

```
uv run python src/carte_aux_tresors/main.py --input data/input_lara.txt --output data/output_lara.txt
```

### Format des fichiers

Les lignes commençant par `#` sont ignorées (commentaires).

#### Fichier d'entrée

```
# {C comme Carte} - {Nb. de case en largeur} - {Nb. de case en hauteur}
C - 3 - 4
# {M comme Montagne} - {Axe horizontal} - {Axe vertical}
M - 1 - 0
M - 2 - 1
# {T comme Trésor} - {Axe horizontal} - {Axe vertical} - {Nb. de trésors}
T - 0 - 3 - 2
T - 1 - 3 - 3
# {A comme Aventurier} - {Nom de l’aventurier} - {Axe horizontal} - {Axe vertical} - {Orientation} - {Séquence de mouvement}
A - Lara - 1 - 1 - S - AADADAGGA
```

#### Fichier de sortie

```
# {C comme Carte} - {Nb. de case en largeur} - {Nb. de case en hauteur}
C - 3 - 4
# {M comme Montagne} - {Axe horizontal} - {Axe vertical}
M - 1 - 0
M - 2 - 1
# {T comme Trésor} - {Axe horizontal} - {Axe vertical} - {Nb. de trésors restants}
T - 1 - 3 - 2
# {A comme Aventurier} - {Nom de l’aventurier} - {Axe horizontal} - {Axe vertical} - {Orientation} - {Nb. trésors ramassés}
A - Lara - 0 - 3 - S - 3
```

## Lancer les tests

```
uv run pytest
```

## Structure du projet

```
.
├── LICENSE
├── README.md
├── data                                    # Fichiers d'entrée/sortie utilisés pour tester le programme
│   ├── input_exemple1.txt                  # Exemple de fichier d'entrée pour tester le programme
│   └── output_exemple1.txt                 # Fichier de sortie avec les résultats générés
├── pyproject.toml                          # Configuration (dépendances)
├── src
│   └── carte_aux_tresors
│       ├── __init__.py
│       ├── main.py
│       ├── models.py                       # Objets Orientation et Adventurer
│       ├── parser.py                       # Lecture et parsing
│       ├── simulation.py                   # Simulation tour par tour
│       └── writer.py                       # Ecriture du fichier de sortie
├── tests                                   # Tests
│   └── fixtures                            # Fichiers d'entrée/sortie utilisés par les tests
│       └── expected_output_exemple1.txt
└── uv.lock
```

## Choix techniques

- **uv** pour la gestion du projet (dépendances, version Python, environnement virtuel).
- **Simulation tour par tour**
- **`argparse`** pour les arguments en ligne de commande.

## Pistes d'amélioration

Si le temps le permettait, voici ce que j'améliorerais :

- Validation plus stricte de certains champs (ex: nom d'aventurier)
- Exceptions métier dédiées plutôt que des `ValueError` génériques
- Logging structuré plutôt que des `print()` pour les erreurs
- Tests de conflits avec plus de deux aventuriers
