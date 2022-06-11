import unittest
from typings import RoverPosition, RoverMission
from mars_rover import max_num_of_commands


class TestRoverUtils(unittest.TestCase):
    def test_max_num_of_commands_3(self):
        rover_missions_with_max_3 = [
                RoverMission(RoverPosition(1, 2, "N"), "LML"),
                RoverMission(RoverPosition(3, 3, "E"), "MM")
            ]
        self.assertEqual(max_num_of_commands(rover_missions_with_max_3), 3)

    def test_max_num_of_commands_2(self):
        rover_missions_with_max_2 = [
                RoverMission(RoverPosition(1, 2, "N"), "L"),
                RoverMission(RoverPosition(3, 3, "E"), "MM")
            ]
        self.assertEqual(max_num_of_commands(rover_missions_with_max_2), 2)