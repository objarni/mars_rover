import sys
from io import TextIOWrapper
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


def extract_mission_data_from_file(file_handle: TextIOWrapper) -> tuple[Coordinate, list[RoverMission]]:
    try:
        x, y = file_handle.readline().strip().split()
        bounds = Coordinate(int(x), int(y))

        missions = []
        for i, line in enumerate(file_handle.readlines()):
            if i % 2 == 0:
                x, y, direction = line.strip().split()
                starting_position = RoverPosition(int(x), int(y), direction)
            else:
                command_sequence = line.strip()
                missions.append(RoverMission(
                    starting_position, command_sequence))

    except:
        exit_with_error_message(
            "Mission data could not be correctly extracted from file. Isn't it encrypted?"
        )


    if ((bounds.x <= 0) or (bounds.y <= 0)):
        exit_with_error_message(
            f"Malformed mission plateau data ({bounds.x}, {bounds.y}). Please measure the mission plateau again.")

    if i % 2 == 0 or not missions:
        exit_with_error_message(
            "Mission data is missing some line. Is the file complete?")

    for starting_position, command_sequence in missions:
        if not (0 <= starting_position.x <= bounds.x and 0 <= starting_position.y <= bounds.y):
            exit_with_error_message(
                f"Rover set to start out of the plateau at position {starting_position}")

        if any(command not in "LRM" for command in command_sequence):
            exit_with_error_message(
                f"Invalid command found in sequence '{command_sequence}'. Was the transmission noisy?")

    return(bounds, missions)


def exit_with_error_message(message: str) -> None:
    print(message)
    sys.exit(0)


if __name__ == "__main__":
    if(len(sys.argv) > 0):
        filename = sys.argv[1]
    else:
        filename = input("Write mission data file name: ")

    try:
        with open(filename, 'rt', encoding='utf-8') as mission_file:
            plateau_bounds, rover_missions = extract_mission_data_from_file(
                mission_file)

        mission_results = execute_mission(plateau_bounds, rover_missions)

        print("Rover final position(s):")
        for rover_position in mission_results:
            print(rover_position)

    except FileNotFoundError:
        print(
            f"Mission data file '{filename}' could not be found. Isn't it top secret?")

    except (BoundsError, CollisionError, CommandError) as error:
        print(error.message)
