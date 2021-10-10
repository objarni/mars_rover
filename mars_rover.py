from typings import RoverPosition, Coordinate, PositionList, PlateauSize, RoverMission
from exceptions import RoverPositionError, OccupiedPositionError, CommandError


def execute_mission(
    plateau_size: PlateauSize,
    rover_missions: list[RoverMission]
) -> list[RoverPosition]:

    ending_positions = PositionList([])
    for (starting_position, command_sequence) in rover_missions:
        rover_position = starting_position

        for command in command_sequence.upper():
            rover_position = process_command(
                command,
                rover_position,
                plateau_size
            )

        if ending_positions.is_occupied(rover_position.get_coordinate()):
            raise OccupiedPositionError(rover_position.get_coordinate())

        ending_positions.append(rover_position)

    return ending_positions


def process_command(
    command: str,
    rover_position: RoverPosition,
    plateau_size: PlateauSize
) -> RoverPosition:

    if command in 'LR':
        return turn_rover(rover_position, command)

    if command == "M":
        return move_rover(rover_position, plateau_size)

    raise CommandError(command)


def turn_rover(rover: RoverPosition, turn_to: str) -> RoverPosition:
    directions = ("N", "E", "S", "W")
    turn_to_translation = {"R": 1, "L": -1}

    new_direction = directions[(
        directions.index(rover.direction) +
        turn_to_translation[turn_to] + len(directions)
    ) % len(directions)]

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
