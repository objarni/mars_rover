from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str


class PlateauSize(NamedTuple):
    x: int
    y: int
