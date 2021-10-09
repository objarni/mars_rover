directions = ("N", "E", "S", "W")


def execute_mission(plateau_size: tuple[int, int], starting_positions: list[tuple[int, int, str]], command_sequences: list[str]) -> list[tuple[int, int, str]]:
    ending_positions = []
    for (starting_position, command_sequence) in zip(starting_positions, command_sequences):
        rover = {
            "x": starting_position[0], "y": starting_position[1], "direction": starting_position[2]}

        for command in command_sequence.upper():
            if command == 'L':
                rover["direction"] = directions[(
                    directions.index(rover["direction"]) + 3) % 4]
            elif command == 'R':
                rover["direction"] = directions[(
                    directions.index(rover["direction"]) + 5) % 4]
            else:
                if rover["direction"] == "N":
                    rover["y"] += 1
                elif rover["direction"] == "E":
                    rover["x"] += 1
                elif rover["direction"] == "S":
                    rover["y"] -= 1
                elif rover["direction"] == "W":
                    rover["x"] -= 1

        ending_positions.append((rover["x"], rover["y"], rover["direction"]))

    return ending_positions
