from typings import PlateauSize


class RoverPositionError(Exception):
    """Exception raised for rover position out of bounds.

    Attributes:
        rover_position -- offending position
        plateau_size -- size of the plateau
        message -- explanation of the error
    """

    def __init__(self, rover_position: tuple[int, int], plateau_size: PlateauSize, message=None):
        self.rover_position = rover_position
        self.plateau_size = plateau_size
        self.message = message or f"Rover position {self.rover_position} is out of bounds of {self.plateau_size}-sized plateau"
