from typings import RoverPosition, Coordinate, PositionList, RoverMission
from exceptions import RoverPositionError, CollisionError, CommandError


command_translation = {
    "N": {
        "L": "W",
        "R": "E",
        "M": Coordinate(0, 1)
    },
    "E": {
        "L": "N",
        "R": "S",
        "M": Coordinate(1, 0)
    },
    "S": {
        "L": "E",
        "R": "W",
        "M": Coordinate(0, -1)
    },
    "W": {
        "L": "S",
        "R": "N",
        "M": Coordinate(-1, 0)
    },
}


def execute_mission(
    plateau_bounds: Coordinate,
    rover_missions: list[RoverMission]
) -> list[RoverPosition]:

    rover_positions = PositionList(
        [mission.starting_position for mission in rover_missions])

    for i, (_, command_sequence) in enumerate(rover_missions):
        for command in command_sequence.upper():
            rover_positions[i] = process_command(
                command,
                rover_positions[i],
                plateau_bounds,
                rover_positions
            )

    return rover_positions


def process_command(
    command: str,
    rover_position: RoverPosition,
    plateau_bounds: Coordinate,
    rover_positions: PositionList
) -> RoverPosition:

    if command in 'LR':
        return turn_rover(rover_position, side=command)

    if command == "M":
        return move_rover(rover_position, plateau_bounds, rover_positions)

    raise CommandError(command)


def turn_rover(rover: RoverPosition, side: str) -> RoverPosition:
    return RoverPosition(
        rover.x,
        rover.y,
        command_translation[rover.direction][side]
    )


def move_rover(
    rover: RoverPosition,
    plateau_bounds: Coordinate,
    rover_positions: PositionList
) -> RoverPosition:

    translation = command_translation[rover.direction]["M"]
    x, y = rover.x + translation.x, rover.y + translation.y

    if rover_positions.is_occupied((x, y)):
        raise CollisionError((x, y))

    if not ((0 <= x <= plateau_bounds.x) and (0 <= y <= plateau_bounds.y)):
        raise RoverPositionError((x, y), plateau_bounds)

    return RoverPosition(x, y, rover.direction)
