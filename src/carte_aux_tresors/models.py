from enum import Enum


class Map:
    """Class representing a map with a width and height.
    Attributes:
        width (int): The width of the map.
        height (int): The height of the map.
    """

    def __init__(
        self,
        width: int,
        height: int,
        mountains: list[tuple[int, int]],
        treasures: dict[tuple[int, int], int],
    ):
        self.width = width
        self.height = height
        self._mountains = mountains
        self._treasures = treasures

    def is_valid_position(self, x: int, y: int) -> bool:
        """Return True if the position is within bounds and not a mountain."""
        in_bounds = 0 <= x < self.width and 0 <= y < self.height
        is_mountain = (x, y) in self._mountains
        return in_bounds and not is_mountain

    def collect_treasure_at(self, x: int, y: int) -> bool:
        """Collect one treasure at the given position, if any remain. Returns True if collected."""
        if self._treasures.get((x, y), 0) > 0:
            self._treasures[(x, y)] -= 1
            return True
        return False

    def remaining_treasures(self) -> dict[tuple[int, int], int]:
        """Return the treasures still present on the map."""
        return {pos: count for pos, count in self._treasures.items() if count > 0}

    def mountains_list(self) -> list[tuple[int, int]]:
        """Return the list of mountain positions."""
        return list(self._mountains)


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
