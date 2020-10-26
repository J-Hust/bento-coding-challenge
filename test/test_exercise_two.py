import unittest
from src.two import count_recurring

class TestExerciseTwo(unittest.TestCase):

    def test_no_repeating(self):
        result = count_recurring('abcd')
        self.assertEqual(result, 'abcd')

    def test_one_reapeating(self):
        result = count_recurring('abbbcd')
        self.assertEqual(result, 'ab3cd')

    def test_repeating_at_end(self):
        result = count_recurring('abbbcddd')
        self.assertEqual(result, 'ab3cd3')

    def test_all_recurring(self):
        result = count_recurring('rrdd')
        self.assertEqual(result, 'r2d2')

    def test_not_repeating_at_end(self):
        result = count_recurring('aabbcdde')
        self.assertEqual(result, 'a2b2cd2e')


if __name__ == '__main__':
    unittest.main()

