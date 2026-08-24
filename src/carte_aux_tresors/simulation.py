from carte_aux_tresors.models import Adventurer, Map


def run_simulation(game_map: Map, adventurers: list[Adventurer]) -> None:
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
                is_occupied = any(
                    a.x == new_x and a.y == new_y
                    for a in adventurers
                    if a is not adventurer
                )

                if game_map.is_valid_position(new_x, new_y) and not is_occupied:
                    adventurer.x, adventurer.y = new_x, new_y
                    if game_map.collect_treasure_at(new_x, new_y):
                        adventurer.treasure_count += 1
