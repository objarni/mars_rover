from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str


class Coordinate(NamedTuple):
    x: int
    y: int


class PlateauSize(Coordinate):
    pass
