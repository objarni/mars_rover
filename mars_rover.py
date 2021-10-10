from typings import RoverPosition, Coordinate, PlateauSize
from exceptions import RoverPositionError, OccupiedPositionError


def execute_mission(
    plateau_size: PlateauSize,
    starting_positions: list[RoverPosition],
    command_sequences: list[str]
) -> list[RoverPosition]:

    ending_positions = []
    for (starting_position, command_sequence) in zip(starting_positions, command_sequences):
        rover_position = starting_position

        for command in command_sequence.upper():
            if command in 'LR':
                rover_position = turn_rover(rover_position, command)
            else:
                rover_position = move_rover(rover_position, plateau_size)

        if rover_position.get_coordinate() in get_coordinates(ending_positions):
            raise OccupiedPositionError(rover_position.get_coordinate())

        ending_positions.append(rover_position)

    return ending_positions


def turn_rover(rover: RoverPosition, turn_to: str) -> RoverPosition:
    directions = ("N", "E", "S", "W")

    new_direction = directions[(
        directions.index(rover.direction) + 4
        + (1 if turn_to == 'R' else -1)
    ) % 4]

    return RoverPosition(rover.x, rover.y, new_direction)


def move_rover(rover: RoverPosition, plateau_size: PlateauSize) -> RoverPosition:
    direction_translation = {
        "N": Coordinate(0, 1),
        "E": Coordinate(1, 0),
        "S": Coordinate(0, -1),
        "W": Coordinate(-1, 0)
    }

    translation = direction_translation[rover.direction]
    x, y = rover.x + translation.x, rover.y + translation.y

    if (0 <= x <= plateau_size.x) and (0 <= y <= plateau_size.y):
        return RoverPosition(x, y, rover.direction)

    raise RoverPositionError((x, y), plateau_size)


def get_coordinates(positions: list[RoverPosition]) -> tuple[Coordinate]:
    return (Coordinate(pos.x, pos.y) for pos in positions)
