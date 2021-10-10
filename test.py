import mars_rover
import unittest
from typings import Coordinate, RoverPosition, RoverMission
from exceptions import BoundsError, CollisionError, CommandError


class TestMarsRover(unittest.TestCase):
    def test_given_example(self):
        ending_positions = mars_rover.execute_mission(
            Coordinate(5, 5),
            [
                RoverMission(RoverPosition(1, 2, "N"), "LMLMLMLMM"),
                RoverMission(RoverPosition(3, 3, "E"), "MMRMMRMRRM")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(1, 3, "N"),
            RoverPosition(5, 1, "E")
        ])

    def test_turns_rover_left(self):
        ending_positions = mars_rover.execute_mission(
            Coordinate(1, 1),
            [
                RoverMission(RoverPosition(0, 0, "N"), "L"),
                RoverMission(RoverPosition(0, 1, "E"), "L"),
                RoverMission(RoverPosition(1, 0, "S"), "L"),
                RoverMission(RoverPosition(1, 1, "W"), "L")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(0, 0, "W"),
            RoverPosition(0, 1, "N"),
            RoverPosition(1, 0, "E"),
            RoverPosition(1, 1, "S")
        ])

    def test_turns_rover_right(self):
        ending_positions = mars_rover.execute_mission(
            Coordinate(1, 1),
            [
                RoverMission(RoverPosition(0, 0, "N"), "R"),
                RoverMission(RoverPosition(0, 1, "E"), "R"),
                RoverMission(RoverPosition(1, 0, "S"), "R"),
                RoverMission(RoverPosition(1, 1, "W"), "R")
            ]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(0, 0, "E"),
            RoverPosition(0, 1, "S"),
            RoverPosition(1, 0, "W"),
            RoverPosition(1, 1, "N")
        ])

    def test_move_directions(self):
        ending_positions = mars_rover.execute_mission(
            Coordinate(2, 2),
            [
                RoverMission(RoverPosition(0, 1, "N"), "M"),
                RoverMission(RoverPosition(0, 0, "E"), "M"),
                RoverMission(RoverPosition(2, 1, "S"), "M"),
                RoverMission(RoverPosition(1, 1, "W"), "M")
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
            BoundsError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [RoverMission(RoverPosition(1, 0, "E"), "M")]
        )

    def test_out_of_bounds_north_raises(self):
        self.assertRaises(
            BoundsError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [RoverMission(RoverPosition(0, 1, "N"), "M")]
        )

    def test_out_of_bounds_west_raises(self):
        self.assertRaises(
            BoundsError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [RoverMission(RoverPosition(0, 1, "W"), "M")]
        )

    def test_out_of_bounds_south_raises(self):
        self.assertRaises(
            BoundsError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [RoverMission(RoverPosition(1, 0, "S"), "M")]
        )

    def test_rovers_ending_in_same_position_raises(self):
        self.assertRaises(
            CollisionError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [
                RoverMission(RoverPosition(0, 1, "S"), "M"),
                RoverMission(RoverPosition(1, 0, "W"), "M")
            ]
        )

    def test_collision_with_finished_rover(self):
        self.assertRaises(
            CollisionError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [
                RoverMission(RoverPosition(0, 1, "S"), "M"),
                RoverMission(RoverPosition(1, 0, "W"), "MRM")
            ]
        )

    def test_collision_with_not_started_rover(self):
        self.assertRaises(
            CollisionError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [
                RoverMission(RoverPosition(0, 1, "S"), "M"),
                RoverMission(RoverPosition(0, 0, "N"), "M")
            ]
        )

    def test_invalid_command_raises(self):
        self.assertRaises(
            CommandError,
            mars_rover.execute_mission,
            Coordinate(1, 1),
            [RoverMission(RoverPosition(0, 0, "N"), "I")],
        )


if __name__ == '__main__':
    unittest.main()
