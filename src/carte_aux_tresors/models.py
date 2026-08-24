from enum import Enum


class Orientation(Enum):
    """Enum representing the orientation."""

    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def turn_right(self) -> "Orientation":
        """Return to the right orientation based on the current orientation."""
        direction = list(Orientation)
        new_index = (direction.index(self) + 1) % len(direction)
        return direction[new_index]

    def turn_left(self) -> "Orientation":
        """Return to the left orientation based on the current orientation."""
        direction = list(Orientation)
        new_index = (direction.index(self) - 1) % len(direction)
        return direction[new_index]

    def move_forward(self, x: int, y: int) -> tuple[int, int]:
        """Return the new position after moving forward based on the current orientation."""
        if self == Orientation.N:
            return x, y - 1
        elif self == Orientation.E:
            return x + 1, y
        elif self == Orientation.S:
            return x, y + 1
        elif self == Orientation.W:
            return x - 1, y


class Adventurer:
    """Class representing an adventurer with a name, position, orientation, sequence of movements.
    Attributes:
        name (str): The name of the adventurer.
        x (int): The x-coordinate of the adventurer's position.
        y (int): The y-coordinate of the adventurer's position.
        orientation (Orientation): The orientation of the adventurer.
        movements (str): The sequence of movements for the adventurer.
        treasure_count (int): The number of treasures collected by the adventurer.
    """

    def __init__(
        self, name: str, x: int, y: int, orientation: Orientation, movements: str
    ):
        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation
        self.movements = movements
        self.treasure_count = 0
