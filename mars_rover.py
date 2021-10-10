from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str


directions = ("N", "E", "S", "W")


def execute_mission(
    plateau_size: tuple[int, int],
    starting_positions: list[tuple[int, int, str]],
    command_sequences: list[str]
) -> list[tuple[int, int, str]]:

    ending_positions = []
    for (starting_position, command_sequence) in zip(starting_positions, command_sequences):
        rover = RoverPosition(
            starting_position[0], starting_position[1], starting_position[2])

        for command in command_sequence.upper():
            if command in 'LR':
                rover = turn_rover(rover, command)
            else:
                rover = move_rover(rover)

        ending_positions.append(tuple(rover))

    return ending_positions


def turn_rover(rover: RoverPosition, turn_to: str) -> RoverPosition:
    new_direction = directions[(
        directions.index(rover.direction) + 4
        + (1 if turn_to == 'R' else -1)
    ) % 4]

    return RoverPosition(rover.x, rover.y, new_direction)


def move_rover(rover: RoverPosition) -> RoverPosition:
    x, y = rover.x, rover.y

    if rover.direction == "N":
        y += 1
    elif rover.direction == "E":
        x += 1
    elif rover.direction == "S":
        y -= 1
    elif rover.direction == "W":
        x -= 1

    return RoverPosition(x, y, rover.direction)
