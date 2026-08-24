from carte_aux_tresors.models import Adventurer


def run_simulation(
    map_width: int,
    map_height: int,
    mountains: list[tuple[int, int]],
    treasures: dict[tuple[int, int], int],
    adventurers: list[Adventurer],
) -> None:
    """Run the simulation, turn by turn."""
    max_movements = max(len(a.movements) for a in adventurers)

    for i in range(max_movements):
        for adventurer in adventurers:
            if i >= len(adventurer.movements):
                continue  # Adventurer has no more movements

            move = adventurer.movements[i]

            if move == "G":
                adventurer.orientation = adventurer.orientation.turn_left()
            elif move == "D":
                adventurer.orientation = adventurer.orientation.turn_right()
            elif move == "A":
                new_x, new_y = adventurer.orientation.move_forward(
                    adventurer.x, adventurer.y
                )

                in_bounds = 0 <= new_x < map_width and 0 <= new_y < map_height
                is_mountain = (new_x, new_y) in mountains
                is_occupied = any(
                    a.x == new_x and a.y == new_y
                    for a in adventurers
                    if a is not adventurer
                )

                if in_bounds and not is_mountain and not is_occupied:
                    adventurer.x, adventurer.y = new_x, new_y
                    if (new_x, new_y) in treasures and treasures[(new_x, new_y)] > 0:
                        adventurer.treasure_count += 1
                        treasures[(new_x, new_y)] -= 1
