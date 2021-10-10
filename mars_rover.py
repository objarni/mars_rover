from typings import RoverPosition, Coordinate, PositionList, PlateauSize, RoverMission
from exceptions import RoverPositionError, CollisionError, CommandError


def execute_mission(
    plateau_size: PlateauSize,
    rover_missions: list[RoverMission]
) -> list[RoverPosition]:

    rover_positions = PositionList(
        [mission.starting_position for mission in rover_missions])

    for i, (_, command_sequence) in enumerate(rover_missions):
        for command in command_sequence.upper():
            rover_positions[i] = process_command(
                command,
                rover_positions[i],
                plateau_size,
                rover_positions
            )

    return rover_positions


def process_command(
    command: str,
    rover_position: RoverPosition,
    plateau_size: PlateauSize,
    ending_positions: PositionList
) -> RoverPosition:

    if command in 'LR':
        return turn_rover(rover_position, command)

    if command == "M":
        return move_rover(rover_position, plateau_size, ending_positions)

    raise CommandError(command)


def turn_rover(rover: RoverPosition, turn_to: str) -> RoverPosition:
    directions = ("N", "E", "S", "W")
    turn_to_translation = {"R": 1, "L": -1}

    new_direction = directions[(
        directions.index(rover.direction) +
        turn_to_translation[turn_to] + len(directions)
    ) % len(directions)]

    return RoverPosition(rover.x, rover.y, new_direction)


def move_rover(
    rover: RoverPosition,
    plateau_size: PlateauSize,
    ending_positions: PositionList
) -> RoverPosition:

    direction_translation = {
        "N": Coordinate(0, 1),
        "E": Coordinate(1, 0),
        "S": Coordinate(0, -1),
        "W": Coordinate(-1, 0)
    }

    translation = direction_translation[rover.direction]
    x, y = rover.x + translation.x, rover.y + translation.y

    if ending_positions.is_occupied((x, y)):
        raise CollisionError((x, y))

    if not ((0 <= x <= plateau_size.x) and (0 <= y <= plateau_size.y)):
        raise RoverPositionError((x, y), plateau_size)

    return RoverPosition(x, y, rover.direction)
