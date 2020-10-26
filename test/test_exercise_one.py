import unittest
from src import one


class TestExerciseOne(unittest.TestCase):

    def test_format_zero(self):
        result = one.format_size(0)
        self.assertEqual(result, '0 B')

    def test_format_bytes(self):
        result = one.format_size(123)
        self.assertEqual(result, '123 B')

    def test_format_kb(self):
        result = one.format_size(1234)
        self.assertEqual(result,'1.21 KB')

    def test_format_mb(self):
        result = one.format_size(1234567)
        self.assertEqual(result, '1.18 MB')

    def test_format_gb(self):
        result = one.format_size(4567000000)
        self.assertEqual(result, '4.25 GB')

    def test_format_tb(self):
        result = one.format_size(7890000000000)
        self.assertEqual(result, '7.18 TB')