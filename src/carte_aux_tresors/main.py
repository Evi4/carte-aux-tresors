import argparse
import sys

from carte_aux_tresors.parser import parse_input
from carte_aux_tresors.simulation import run_simulation
from carte_aux_tresors.writer import write_output


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="La carte aux trésors")
    parser.add_argument(
        "--input", required=True, type=str, help="Chemin vers le fichier d'entrée"
    )
    parser.add_argument(
        "--output", required=True, type=str, help="Chemin vers le fichier de sortie"
    )

    args = parser.parse_args()

    try:
        map_width, map_height, mountains, treasures, adventurers = parse_input(
            args.input
        )
    except FileNotFoundError:
        print(f"Le fichier d'entrée '{args.input}' est introuvable.")
        sys.exit(1)
    except ValueError as error:
        print(f"Le fichier d'entrée est invalide : {error}")
        sys.exit(1)

    run_simulation(map_width, map_height, mountains, treasures, adventurers)
    write_output(args.output, map_width, map_height, mountains, treasures, adventurers)


if __name__ == "__main__":
    main()
