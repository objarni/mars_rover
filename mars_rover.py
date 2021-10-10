from typing import NamedTuple


class Rover(NamedTuple):
    x: int
    y: int
    direction: str


directions = ("N", "E", "S", "W")


def execute_mission(plateau_size: tuple[int, int], starting_positions: list[tuple[int, int, str]], command_sequences: list[str]) -> list[tuple[int, int, str]]:
    ending_positions = []
    for (starting_position, command_sequence) in zip(starting_positions, command_sequences):
        rover = Rover(
            starting_position[0], starting_position[1], starting_position[2])

        for command in command_sequence.upper():
            if command in 'LR':
                rover = turn_rover(rover, command)
            else:
                rover = move_rover(rover)

        ending_positions.append(tuple(rover))

    return ending_positions


def turn_rover(rover: Rover, turn_to: str) -> Rover:
    new_direction = directions[(
        directions.index(rover.direction) + 4
        + (1 if turn_to == 'R' else -1)
    ) % 4]

    return Rover(rover.x, rover.y, new_direction)


def move_rover(rover: Rover) -> Rover:
    x, y = rover.x, rover.y

    if rover.direction == "N":
        y += 1
    elif rover.direction == "E":
        x += 1
    elif rover.direction == "S":
        y -= 1
    elif rover.direction == "W":
        x -= 1

    return Rover(x, y, rover.direction)
