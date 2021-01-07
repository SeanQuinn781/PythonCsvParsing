import unittest
from Part1 import get_lowest_temp, get_lowest_temp_pd, get_lowest_temp_slowest
from Part2 import get_temp_flucs
from Part2Pandas import get_temp_flucs_pd
from Part3 import get_temp_flucs_date_range


class TestTempFuncs(unittest.TestCase):

    # Test functions in part 1 (tests 3 different functions with 3 different data sets)
    def test_get_lowest_temp(self):
        self.assertEqual(get_lowest_temp("Data/test-data-1.csv"), ('68', '2000.375'))
        self.assertEqual(get_lowest_temp_pd("Data/test-data.csv"), (68.0, 2000.542))
        self.assertEqual(
            get_lowest_temp("Data/test-data-2.csv"), ("68", "2000.375")
        )
        self.assertEqual(get_lowest_temp_pd("Data/data.csv"), (676223.0, 2010.542))

    # Test functions in part 2
    def test_get_temp_flucs(self):
        self.assertEqual(get_temp_flucs("Data/test-data-1.csv"), 865329)
        self.assertEqual(get_temp_flucs("Data/test-data-2.csv"), 420000)
        self.assertEqual(get_temp_flucs("Data/test-data.csv"), 68)
        # self.assertEqual(get_temp_flucs_pd("Data/data.csv"), 757524)

    # Test function in part 3
    def test_get_temp_flucs_date_range(self):
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data-1.csv", 2000.001, 2011.8), 865329
        )
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data-2.csv", 2000.001, 2011.8), 420000
        )
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data.csv", 2000.001, 2011.8), 68
        )
        # self.assertEqual(get_temp_flucs_date_range("Data/data.csv", 2000.001, 2011.8), 735181)


if __name__ == "__main__":
    unittest.main()
