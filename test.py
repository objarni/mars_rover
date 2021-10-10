import mars_rover
import unittest
from typings import PlateauSize, RoverPosition
from exceptions import RoverPositionError, CollisionError, CommandError


class TestMarsRover(unittest.TestCase):
    def test_given_example(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(5, 5),
            [
                (RoverPosition(1, 2, "N"), "LMLMLMLMM"),
                (RoverPosition(3, 3, "E"), "MMRMMRMRRM")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(1, 3, "N"),
            RoverPosition(5, 1, "E")
        ])

    def test_turns_rover_left(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [
                (RoverPosition(0, 0, "N"), "L"),
                (RoverPosition(0, 0, "E"), "L"),
                (RoverPosition(0, 0, "S"), "L"),
                (RoverPosition(0, 0, "W"), "L")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(0, 0, "W"),
            RoverPosition(0, 0, "N"),
            RoverPosition(0, 0, "E"),
            RoverPosition(0, 0, "S")
        ])

    def test_turns_rover_right(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [
                (RoverPosition(0, 0, "N"), "R"),
                (RoverPosition(0, 0, "E"), "R"),
                (RoverPosition(0, 0, "S"), "R"),
                (RoverPosition(0, 0, "W"), "R")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(0, 0, "E"),
            RoverPosition(0, 0, "S"),
            RoverPosition(0, 0, "W"),
            RoverPosition(0, 0, "N")
        ])

    def test_move_directions(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(2, 2),
            [
                (RoverPosition(0, 1, "N"), "M"),
                (RoverPosition(0, 0, "E"), "M"),
                (RoverPosition(2, 1, "S"), "M"),
                (RoverPosition(1, 1, "W"), "M")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(0, 2, "N"),
            RoverPosition(1, 0, "E"),
            RoverPosition(2, 0, "S"),
            RoverPosition(0, 1, "W")
        ])

    def test_out_of_bounds_east_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [(RoverPosition(1, 0, "E"), "M")]
        )

    def test_out_of_bounds_north_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [(RoverPosition(0, 1, "N"), "M")]
        )

    def test_out_of_bounds_west_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [(RoverPosition(0, 1, "W"), "M")]
        )

    def test_out_of_bounds_south_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [(RoverPosition(1, 0, "S"), "M")]
        )

    def test_rovers_ending_in_same_position_raises(self):
        self.assertRaises(
            CollisionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [
                (RoverPosition(0, 1, "S"), "M"),
                (RoverPosition(1, 0, "W"), "M")
            ]
        )

    def test_rover_collision_during_movement(self):
        self.assertRaises(
            CollisionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [
                (RoverPosition(0, 1, "S"), "M"),
                (RoverPosition(1, 0, "W"), "MRM")
            ]
        )

    def test_invalid_command_raises(self):
        self.assertRaises(
            CommandError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "N"), "I")],
        )


if __name__ == '__main__':
    unittest.main()
