import unittest
from src import one


class TestExerciseOne(unittest.TestCase):

    def test_format_zero(self):
        result = one.format_size(0)
        self.assertEqual(result, '0 B')

    def test_format_bytes(self):
        pass

    def test_format_kb(self):
        pass

    def test_format_mb(self):
        pass

    def test_format_gb(self):
        pass

    def test_format_tb(self):
        pass