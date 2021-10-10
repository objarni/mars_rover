from typings import RoverPosition, Coordinate, PlateauSize
from exceptions import RoverPositionError


def execute_mission(
    plateau_size: PlateauSize,
    starting_positions: list[RoverPosition],
    command_sequences: list[str]
) -> list[RoverPosition]:

    ending_positions = []
    for (starting_position, command_sequence) in zip(starting_positions, command_sequences):
        rover = RoverPosition(
            starting_position[0], starting_position[1], starting_position[2])

        for command in command_sequence.upper():
            if command in 'LR':
                rover = turn_rover(rover, command)
            else:
                rover = move_rover(rover, plateau_size)

        ending_positions.append(rover)

    return ending_positions


def turn_rover(rover: RoverPosition, turn_to: str) -> RoverPosition:
    directions = ("N", "E", "S", "W")

    new_direction = directions[(
        directions.index(rover.direction) + 4
        + (1 if turn_to == 'R' else -1)
    ) % 4]

    return RoverPosition(rover.x, rover.y, new_direction)


def move_rover(rover: RoverPosition, plateau_size: PlateauSize) -> RoverPosition:
    directionTranslation = {
        "N": Coordinate(0, 1),
        "E": Coordinate(1, 0),
        "S": Coordinate(0, -1),
        "W": Coordinate(-1, 0)
    }

    translation = directionTranslation[rover.direction]
    x, y = rover.x + translation.x, rover.y + translation.y

    if (0 <= x <= plateau_size.x) and (0 <= y <= plateau_size.y):
        return RoverPosition(x, y, rover.direction)

    raise RoverPositionError((x, y), plateau_size)
