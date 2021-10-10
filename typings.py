from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str

    def get_coordinate(self):
        return (self.x, self.y)


class Coordinate(NamedTuple):
    x: int
    y: int


class PositionList(list):
    def is_occupied(self, coordinate: Coordinate) -> bool:
        return any(coordinate == pos.get_coordinate() for pos in self)


class PlateauSize(Coordinate):
    pass


class RoverMission(NamedTuple):
    starting_position: RoverPosition
    command_sequence: str
