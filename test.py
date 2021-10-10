import mars_rover
import unittest
from typings import PlateauSize, RoverPosition
from exceptions import RoverPositionError


class TestMarsRover(unittest.TestCase):
    def test_given_example(self):
        ending_positions = mars_rover.execute_mission(
            PlateauSize(5, 5),
            [RoverPosition(1, 2, "N"), RoverPosition(3, 3, "E")],
            ["LMLMLMLMM", "MMRMMRMRRM"]
        )

        self.assertEqual(ending_positions, [
            RoverPosition(1, 3, 'N'),
            RoverPosition(5, 1, 'E')
        ])

    def test_out_of_bounds_east_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [RoverPosition(1, 0, "E")],
            ["M"]
        )

    def test_out_of_bounds_north_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [RoverPosition(0, 1, "N")],
            ["M"]
        )

    def test_out_of_bounds_west_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [RoverPosition(0, 1, "W")],
            ["M"]
        )

    def test_out_of_bounds_south_raises(self):
        self.assertRaises(
            RoverPositionError,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [RoverPosition(1, 0, "S")],
            ["M"]
        )

    def test_rovers_in_same_position_raises(self):
        self.assertRaises(
            Exception,
            mars_rover.execute_mission,
            PlateauSize(1, 1),
            [RoverPosition(0, 1, "S"), RoverPosition(1, 0, "W")],
            ["M", "M"]
        )


if __name__ == '__main__':
    unittest.main()
