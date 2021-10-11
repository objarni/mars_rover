from typings import RoverPosition, Coordinate, PositionList, RoverMission
from exceptions import BoundsError, CollisionError, CommandError


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
            )

            check_position_validity(
                rover_positions[i],
                plateau_bounds,
                rover_positions
            )

    return rover_positions


def process_command(
    command: str,
    rover_position: RoverPosition
) -> RoverPosition:

    if command in 'LR':
        return turn_rover(rover_position, side=command)

    if command == "M":
        return move_rover_forward(rover_position)

    raise CommandError(command)


def turn_rover(rover: RoverPosition, side: str) -> RoverPosition:
    return RoverPosition(
        rover.x,
        rover.y,
        command_translation[rover.direction][side]
    )


def move_rover_forward(rover: RoverPosition) -> RoverPosition:

    movement = command_translation[rover.direction]["M"]

    return RoverPosition(
        rover.x + movement.x,
        rover.y + movement.y,
        rover.direction
    )


def check_position_validity(
    rover: RoverPosition,
    plateau_bounds: Coordinate,
    rover_positions: PositionList
) -> None:

    position = rover.get_coordinate()

    if rover_positions.has_collision(position):
        raise CollisionError(position)

    if not ((0 <= position.x <= plateau_bounds.x) and (0 <= position.y <= plateau_bounds.y)):
        raise BoundsError(position, plateau_bounds)


# if __name__ == "__main__":
#     bounds = Coordinate(-1, -1)
#     while bounds.x < 0 or bounds.y < 0:
#         try:
#             x, y = map(int, input(
#                 "Mars exploration plateau horizontal and vertical limit (space separated): ").split())
#             bounds = Coordinate(x, y)
#         except:
#             bounds = Coordinate(-1, -1)

#     missions = []
#     line = '.'
#     while line.strip():
#         try:
#             position = RoverPosition()
#             pass
#         except:
#             line = '.'
