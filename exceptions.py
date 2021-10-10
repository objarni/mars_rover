from typings import Coordinate, PlateauSize


class RoverPositionError(Exception):
    """Exception raised for rover position out of bounds

    Attributes:
        rover_position -- offending position
        plateau_size -- size of the plateau
        message -- explanation of the error
    """

    def __init__(self, rover_position: Coordinate, plateau_size: PlateauSize, message=None) -> None:
        super().__init__()
        self.rover_position = rover_position
        self.plateau_size = plateau_size
        self.message = message or f"Rover position {self.rover_position} is out of bounds of {self.plateau_size}-sized plateau"


class OccupiedPositionError(Exception):
    """Exception raised for rover position in occupied spot

    Attributes:
        rover_position -- offending position
        message -- explanation of the error
    """

    def __init__(self, rover_position: Coordinate, message=None) -> None:
        super().__init__()
        self.rover_position = rover_position
        self.message = message or f"Rover position {self.rover_position} is already occupied"


class CommandError(Exception):
    """Exception raised for invalid command

    Attributes:
        command -- offending command
        message -- explanation of the error
    """

    def __init__(self, command: str, message=None) -> None:
        super().__init__()
        self.command = command
        self.message = message or f"Rover received invalid command {self.command}"
