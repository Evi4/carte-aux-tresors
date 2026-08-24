from carte_aux_tresors.models import Adventurer, Map, Orientation


def parse_input(input_file_path: str) -> tuple[Map, list[Adventurer]]:
    """Parse the input file and return the map dimensions, mountains, treasures, and adventurers.
    Args:
        input_file_path (str): The path to the input file.
    Returns:
        tuple: (map, adventurers) where map is an instance of Map and adventurers is a list of Adventurer instances.
    """
    mountains = []
    treasures = {}
    adventurers = []
    map_width, map_height = (None, None)

    # Read the input file and parse its contents
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if line:  # Line is not empty
                if line.startswith("#"):
                    continue  # Line is a comment

                elif line.startswith("C"):
                    if map_width is not None:
                        raise ValueError(
                            f"La carte ne peut être définie qu'une seule fois. Ligne en trop : '{line}'."
                        )

                    map_line = line.split(" - ")

                    if len(map_line) != 3:
                        raise ValueError(
                            f"Les lignes decrivant la carte doivent contenir 3 elements. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{C comme Carte}} - {{Nb. de case en largeur}} - {{Nb. de case en hauteur}}"
                        )
                    try:
                        map_width, map_height = int(map_line[1]), int(map_line[2])
                    except ValueError:
                        raise ValueError(
                            f"Les dimensions de la carte doivent etre des entiers. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{C comme Carte}} - {{Nb. de case en largeur}} - {{Nb. de case en hauteur}}"
                        )

                    if map_width <= 0 or map_height <= 0:
                        raise ValueError(
                            f"Les dimensions de la carte doivent être des entiers positifs. Ligne incorrecte : '{line}'."
                        )

                elif line.startswith("M"):
                    mountain_line = line.split(" - ")

                    if len(mountain_line) != 3:
                        raise ValueError(
                            f"Les lignes decrivant une montagne doivent contenir 3 elements. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{M comme Montagne}} - {{Axe horizontal}} - {{Axe vertical}}"
                        )
                    try:
                        x, y = int(mountain_line[1]), int(mountain_line[2])
                    except ValueError:
                        raise ValueError(
                            f"Les coordonnees d'une montagne doivent etre des entiers. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{M comme Montagne}} - {{Axe horizontal}} - {{Axe vertical}}"
                        )

                    if x < 0 or y < 0:
                        raise ValueError(
                            f"Les coordonnées d'une montagne doivent être positives ou nulles. Ligne incorrecte : '{line}'."
                        )

                    mountains.append((x, y))

                elif line.startswith("T"):
                    treasure_line = line.split(" - ")

                    if len(treasure_line) != 4:
                        raise ValueError(
                            f"Les lignes decrivant un tresor doivent contenir 4 elements. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{T comme Trésor}} - {{Axe horizontal}} - {{Axe vertical}} - {{Nb. de trésors}}"
                        )

                    try:
                        x, y, treasure_count = (
                            int(treasure_line[1]),
                            int(treasure_line[2]),
                            int(treasure_line[3]),
                        )
                    except ValueError:
                        raise ValueError(
                            f"Les coordonnees et le nombre de trésors doivent etre des entiers. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{T comme Trésor}} - {{Axe horizontal}} - {{Axe vertical}} - {{Nb. de trésors}}"
                        )

                    if x < 0 or y < 0:
                        raise ValueError(
                            f"Les coordonnées d'un trésor doivent être positives ou nulles. Ligne incorrecte : '{line}'."
                        )

                    if treasure_count <= 0:
                        raise ValueError(
                            f"Le nombre de trésors doit être un entier strictement positif. Ligne incorrecte : '{line}'."
                        )

                    treasures[(x, y)] = treasure_count

                elif line.startswith("A"):
                    adventurer_line = line.split(" - ")

                    if len(adventurer_line) != 6:
                        raise ValueError(
                            f"Les lignes decrivant un aventurier doivent contenir 6 elements. Ligne incorrecte : '{line}'.\n"
                            f"Format attendu : {{A comme Aventurier}} - {{Nom de l'aventurier}} - {{Axe horizontal}} - {{Axe vertical}} - {{Orientation}} - {{Séquence de mouvement}}"
                        )

                    name = adventurer_line[1]

                    try:
                        x, y = int(adventurer_line[2]), int(adventurer_line[3])
                    except ValueError:
                        raise ValueError(
                            f"Les coordonnées d'un aventurier doivent être des entiers. Ligne incorrecte : '{line}'."
                        )

                    try:
                        orientation = Orientation(adventurer_line[4])
                    except ValueError:
                        raise ValueError(
                            f"L'orientation d'un aventurier doit être N, E, S ou W. Ligne incorrecte : '{line}'."
                        )

                    movements = adventurer_line[5]
                    if not all(move in "AGD" for move in movements):
                        raise ValueError(
                            f"La séquence de mouvements ne doit contenir que les lettres A, G ou D. Ligne incorrecte : '{line}'."
                        )

                    adventurer = Adventurer(name, x, y, orientation, movements)
                    adventurers.append(adventurer)

                else:
                    raise ValueError(
                        f"Ligne non conforme : '{line}'. Une ligne doit commencer par C, M, T, A ou #."
                    )

    if map_width is None or map_height is None:
        raise ValueError(
            "La carte doit être définie dans le fichier d'entrée avec une ligne commençant par C."
        )

    if not adventurers:
        raise ValueError(
            "Au moins un aventurier doit être défini dans le fichier d'entrée avec une ligne commençant par A."
        )

    return Map(map_width, map_height, mountains, treasures), adventurers
