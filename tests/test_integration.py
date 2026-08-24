from carte_aux_tresors.parser import parse_input
from carte_aux_tresors.simulation import run_simulation
from carte_aux_tresors.writer import write_output


def run_test_simulation(input_path: str, tmp_path) -> str:
    """Run simulation and return the output content."""
    output_file_path = tmp_path / "output.txt"

    game_map, adventurers = parse_input(input_path)
    run_simulation(game_map, adventurers)
    write_output(str(output_file_path), game_map, adventurers)

    return output_file_path.read_text().strip()


def test_simulation_adventurer_lara(tmp_path):
    result = run_test_simulation("tests/fixtures/input_lara.txt", tmp_path)

    with open("tests/fixtures/expected_output_lara.txt", "r") as expected_file:
        expected_content = expected_file.read().strip()

    assert result == expected_content


def test_simulation_adventurer_stuck_at_edges(tmp_path):
    result = run_test_simulation(
        "tests/fixtures/input_adventurer_at_edges.txt", tmp_path
    )

    with open(
        "tests/fixtures/expected_output_adventurer_at_edges.txt", "r"
    ) as expected_file:
        expected_content = expected_file.read().strip()

    assert result == expected_content


def test_simulation_adventurer_stuck_by_mountains(tmp_path):
    result = run_test_simulation(
        "tests/fixtures/input_adventurer_stuck_by_mountains.txt", tmp_path
    )

    with open(
        "tests/fixtures/expected_output_adventurer_stuck_by_mountains.txt", "r"
    ) as expected_file:
        expected_content = expected_file.read().strip()

    assert result == expected_content
