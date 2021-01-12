import unittest
# import non-pandas functions
from part_1 import get_lowest_temp, get_lowest_temp_slowest
from part_2 import get_temp_flucs
from part_3 import get_temp_flucs_date_range

# import pandas functions
from part_1_pandas import get_lowest_temp_pd
from part_2_pandas import get_temp_flucs_pd
from part_3_pandas import get_temp_flucs_date_range_pd

# NOTE: These tests take a while to run due to the large dataset
print("----------------------------------------------------------------------")
print("Testing pandas and non pandas temperature functions on data.csv")
print("NOTE: These tests may take a while")

class TestStringMethods(unittest.TestCase):

    # Test functions in part 1 (tests full data set from data.csv)
    def test_get_lowest_temp(self):
        self.assertEqual(get_lowest_temp("Data/data.csv"), ('676223', '2010.542'))

    # Test functions in part 2
    def test_get_temp_flucs(self):
        self.assertEqual(get_temp_flucs("Data/data.csv"), '735181')

    # Test function in part 3
    def test_get_temp_flucs_date_range(self):
        self.assertEqual(get_temp_flucs_date_range("Data/data.csv", '2000.001', '2011.8'), '735181')

    # ------------------------------- Test Pandas Versions  -------------------------------

    # Test functions in part 1 (tests 3 different functions with 3 different data sets)
    def test_get_lowest_temp_pd(self):
        self.assertEqual(get_lowest_temp_pd("Data/data.csv"), (676223.0, 2010.542))

    # Test functions in part 2
    def test_get_temp_flucs_pd(self):
        self.assertEqual(get_temp_flucs_pd("Data/data.csv"), 757524)

    # Test function in part 3
    def test_get_temp_flucs_date_range_pd(self):
        self.assertEqual(get_temp_flucs_date_range_pd("Data/data.csv", 2000.001, 2011.8), 735181)


if __name__ == "__main__":
    unittest.main()
