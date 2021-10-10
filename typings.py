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


class PlateauSize(Coordinate):
    pass
