import unittest

from parameterized import parameterized

from rover import Rover


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ('R', 'N', 'E'),
        ('R', 'E', 'S'),
        ('R', 'S', 'W'),
        ('R', 'W', 'N')
    ])
    def test_turns_right_clockwise(self, turns, starts_facing, ends_facing):
        rover = Rover(starts_facing)
        rover = rover.go(turns)
        self.assertEqual(ends_facing, rover.facing)

    @parameterized.expand([
        ('L', 'N', 'W'),
        ('L', 'W', 'S'),
        ('L', 'S', 'E'),
        ('L', 'E', 'N'),
    ])
    def test_turns_left_anticlockwise(self, turns, starts_facing, ends_facing):
        rover = Rover(starts_facing)
        rover = rover.go(turns)
        self.assertEqual(ends_facing, rover.facing)


if __name__ == '__main__':
    unittest.main()
