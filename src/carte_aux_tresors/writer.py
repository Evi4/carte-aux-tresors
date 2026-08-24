from carte_aux_tresors.models import Adventurer, Map


def write_output(
    output_file_path: str, game_map: Map, adventurers: list[Adventurer]
) -> None:
    """Write the output to the specified file."""
    with open(output_file_path, "w") as output_file:
        output_file.write(f"C - {game_map.width} - {game_map.height}\n")
        output_file.writelines(f"M - {x} - {y}\n" for x, y in game_map.mountains_list())
        output_file.writelines(f"T - {x} - {y} - {count}\n" for (x, y), count in game_map.remaining_treasures().items())
        output_file.writelines(
            f"A - {adventurer.name} - {adventurer.x} - {adventurer.y} - {adventurer.orientation.value} - {adventurer.treasure_count}\n"
            for adventurer in adventurers
        )
