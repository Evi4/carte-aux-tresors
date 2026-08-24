from carte_aux_tresors.models import Adventurer


def write_output(
    output_file_path: str,
    map_width: int,
    map_height: int,
    mountains: list[tuple[int, int]],
    treasures: dict[tuple[int, int], int],
    adventurers: list[Adventurer],
) -> None:
    """Write the output to the specified file."""
    with open(output_file_path, "w") as output_file:
        output_file.write(f"C - {map_width} - {map_height}\n")
        output_file.writelines(f"M - {x} - {y}\n" for x, y in mountains)
        for (x, y), count in treasures.items():
            if count > 0:  # Only write treasures that are still present
                output_file.write(f"T - {x} - {y} - {count}\n")
        output_file.writelines(
            f"A - {adventurer.name} - {adventurer.x} - {adventurer.y} - {adventurer.orientation.value} - {adventurer.treasure_count}\n"
            for adventurer in adventurers
        )
