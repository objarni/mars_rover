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

    def test_turns_rover_left_from_north(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "N"), "L")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "W")])

    def test_turns_rover_left_from_east(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "E"), "L")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "N")])

    def test_turns_rover_left_from_south(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "S"), "L")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "E")])

    def test_turns_rover_left_from_west(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "W"), "L")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "S")])

    def test_turns_rover_right_from_north(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "N"), "R")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "E")])

    def test_turns_rover_right_from_east(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "E"), "R")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "S")])

    def test_turns_rover_right_from_south(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "S"), "R")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "W")])

    def test_turns_rover_right_from_west(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "W"), "R")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "N")])

    def test_move_north(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "N"), "M")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 1, "N")])

    def test_move_east(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 0, "E"), "M")]
        )

        self.assertEqual(ending_positions, [RoverPosition(1, 0, "E")])

    def test_move_south(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(0, 1, "S"), "M")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "S")])

    def test_move_west(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(1, 1),
            [(RoverPosition(1, 0, "W"), "M")]
        )

        self.assertEqual(ending_positions, [RoverPosition(0, 0, "W")])

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
