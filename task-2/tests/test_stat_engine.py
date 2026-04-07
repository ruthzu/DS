import unittest
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        engine = StatEngine(data)
        self.assertEqual(engine.get_mean(), 3)

    def test_median_odd(self):
        data = [1, 3, 5]
        engine = StatEngine(data)
        self.assertEqual(engine.get_median(), 3)

    def test_median_even(self):
        data = [1, 2, 3, 4]
        engine = StatEngine(data)
        self.assertEqual(engine.get_median(), 2.5)

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)
        self.assertAlmostEqual(engine.get_standard_deviation(), 2.138, places=2)


if __name__ == "__main__":
    unittest.main()