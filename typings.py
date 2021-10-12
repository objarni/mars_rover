from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str

    def get_coordinate(self):
        return Coordinate(self.x, self.y)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction}"


class Coordinate(NamedTuple):
    x: int
    y: int


class PositionList(list):
    def has_collision(self, coordinate: Coordinate) -> bool:
        return sum(map(
            lambda pos: 1 if coordinate == pos.get_coordinate() else 0,
            self)
        ) > 1


class RoverMission(NamedTuple):
    starting_position: RoverPosition
    command_sequence: str
