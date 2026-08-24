from carte_aux_tresors.models import Adventurer, Map, Orientation
from carte_aux_tresors.simulation import run_simulation


def test_simulation_adventurers_blocking_each_other():
    """Test that adventurers cannot move into each other's positions."""
    game_map = Map(3, 3, [], {})
    alice = Adventurer("Alice", 1, 1, Orientation.E, "A")
    bob = Adventurer("Bob", 2, 1, Orientation.W, "A")

    run_simulation(game_map, [alice, bob])

    assert alice.x == 1 and alice.y == 1
    assert bob.x == 2 and bob.y == 1
