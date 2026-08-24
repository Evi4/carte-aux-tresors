import pytest

from carte_aux_tresors.models import Orientation


@pytest.mark.parametrize(
    "orientation, expected",
    [
        (Orientation.N, Orientation.E),
        (Orientation.E, Orientation.S),
        (Orientation.S, Orientation.W),
        (Orientation.W, Orientation.N),
    ],
)
def test_turn_right(orientation, expected):
    assert orientation.turn_right() == expected


@pytest.mark.parametrize(
    "orientation, expected",
    [
        (Orientation.N, Orientation.W),
        (Orientation.W, Orientation.S),
        (Orientation.S, Orientation.E),
        (Orientation.E, Orientation.N),
    ],
)
def test_turn_left(orientation, expected):
    assert orientation.turn_left() == expected


@pytest.mark.parametrize(
    "orientation, initial_position, expected_position",
    [
        (Orientation.N, (1, 1), (1, 0)),
        (Orientation.E, (1, 1), (2, 1)),
        (Orientation.S, (1, 1), (1, 2)),
        (Orientation.W, (1, 1), (0, 1)),
    ],
)
def test_move_forward(orientation, initial_position, expected_position):
    x, y = initial_position
    new_x, new_y = orientation.move_forward(x, y)
    assert (new_x, new_y) == expected_position
