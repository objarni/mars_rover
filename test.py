import mars_rover
import unittest


class TestMarsRover(unittest.TestCase):
    def test_given_example(self):
        ending_positions = mars_rover.execute_mission((5, 5), [(1, 2, "N"), (3, 3, "E")], [
            "LMLMLMLMM", "MMRMMRMRRM"])

        self.assertEqual(ending_positions, [(1, 3, 'N'), (5, 1, 'E')])


if __name__ == '__main__':
    unittest.main()
