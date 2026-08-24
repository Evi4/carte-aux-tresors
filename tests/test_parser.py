import pytest

from carte_aux_tresors.models import Orientation
from carte_aux_tresors.parser import parse_input


def test_parse_input(tmp_path):
    input_file = tmp_path / "test_input.txt"
    input_file.write_text(
        "C - 5 - 6\nM - 2 - 3\nT - 4 - 4 - 2\nA - Dora - 0 - 1 - E - AAGDA\n"
    )

    game_map, adventurers = parse_input(str(input_file))

    assert game_map.width == 5
    assert game_map.height == 6
    assert game_map.is_valid_position(2, 3) is False
    assert game_map.remaining_treasures() == {(4, 4): 2}
    assert len(adventurers) == 1
    assert adventurers[0].name == "Dora"
    assert adventurers[0].x == 0
    assert adventurers[0].y == 1
    assert adventurers[0].orientation == Orientation.E
    assert adventurers[0].movements == "AAGDA"


def test_parse_input_with_multiple_elements(tmp_path):
    """Verify that the parser correctly handles multiple mountains, treasures, and adventurers."""
    input_file = tmp_path / "test_input.txt"
    input_file.write_text(
        "C - 5 - 6\n"
        "M - 1 - 1\n"
        "M - 3 - 3\n"
        "T - 0 - 0 - 2\n"
        "T - 4 - 4 - 5\n"
        "A - Dora - 0 - 1 - E - A\n"
        "A - Boots - 4 - 4 - N - A\n"
    )

    game_map, adventurers = parse_input(str(input_file))

    assert game_map.is_valid_position(1, 1) is False
    assert game_map.is_valid_position(3, 3) is False
    assert game_map.remaining_treasures() == {(0, 0): 2, (4, 4): 5}
    assert len(adventurers) == 2
    assert adventurers[0].name == "Dora"
    assert adventurers[1].name == "Boots"


def test_parse_input_ignores_comments_and_empty_lines(tmp_path):
    """Verify that comments and empty lines are properly ignored."""
    input_file = tmp_path / "test_input.txt"
    input_file.write_text(
        "# Un commentaire\n"
        "C - 5 - 6\n"
        "\n"
        "# Un autre commentaire\n"
        "A - Dora - 0 - 1 - E - A\n"
    )

    game_map, adventurers = parse_input(str(input_file))

    assert game_map.width == 5
    assert game_map.height == 6
    assert len(adventurers) == 1


@pytest.mark.parametrize(
    "file_content, expected_message",
    [
        ("M - 1 - 1\n", "La carte doit être définie"),
        ("C - 3\n", "doivent contenir 3 elements"),
        ("C - trois - 4\n", "doivent etre des entiers"),
        ("C - 0 - 4\n", "doivent être des entiers positifs"),
        ("C - 3 - 4\nC - 5 - 6\n", "ne peut être définie qu'une seule fois"),
        ("C - 3 - 4\nM - 1\n", "montagne doivent contenir 3 elements"),
        ("C - 3 - 4\nM - -1 - 2\n", "doivent être positives ou nulles"),
        ("C - 3 - 4\nT - 1 - 1\n", "tresor doivent contenir 4 elements"),
        ("C - 3 - 4\nT - 1 - 1 - 0\n", "doit être un entier strictement positif"),
        ("C - 3 - 4\nA - Bob - 1 - 1\n", "aventurier doivent contenir 6 elements"),
        ("C - 3 - 4\nA - Bob - 1 - 1 - X - A\n", "doit être N, E, S ou W"),
        (
            "C - 3 - 4\nA - Bob - x - 1 - N - A\n",
            "coordonnées d'un aventurier doivent être des entiers",
        ),
        (
            "C - 3 - 4\nA - Bob - 1 - 1 - N - AGX\n",
            "ne doit contenir que les lettres A, G ou D",
        ),
        ("C - 3 - 4\nX - 1 - 2\n", "Ligne non conforme"),
        ("C - 3 - 4\n", "Au moins un aventurier doit être défini"),
    ],
)
def test_parse_input_raises_on_invalid_input(tmp_path, file_content, expected_message):
    input_file = tmp_path / "invalid_input.txt"
    input_file.write_text(file_content)

    with pytest.raises(ValueError, match=expected_message):
        parse_input(str(input_file))
