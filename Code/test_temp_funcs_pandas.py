import unittest
from part_1_pandas import get_lowest_temp_pd
from part_2_pandas import get_temp_flucs_pd
from part_3_pandas import get_temp_flucs_date_range_pd

# Tests all pandas functions using test data
print("----------------------------------------------------------------------")
print("Testing pandas temperature functions")

class TestTempFuncsPd(unittest.TestCase):

    def test_get_lowest_temp_pd(self):
        self.assertEqual(get_lowest_temp_pd("Data/test-data-1.csv"), (68, 2000.375))
        self.assertEqual(get_lowest_temp_pd("Data/test-data-2.csv"), (68, 2000.375))
        self.assertEqual(get_lowest_temp_pd("Data/test-data.csv"), (1, 2000.375))

    def test_get_temp_flucs_pd(self):
        self.assertEqual(get_temp_flucs_pd("Data/test-data-1.csv"), 865329)
        self.assertEqual(get_temp_flucs_pd("Data/test-data-2.csv"), 420000)
        self.assertEqual(get_temp_flucs_pd("Data/test-data.csv"), 2)

    def test_get_temp_flucs_date_range_pd(self):
        self.assertEqual(
            get_temp_flucs_date_range_pd("Data/test-data-1.csv", 2000.001, 2011.8), 865329
        )
        self.assertEqual(
            get_temp_flucs_date_range_pd("Data/test-data-2.csv", 2000.001, 2011.8), 420000
        )
        self.assertEqual(
            get_temp_flucs_date_range_pd("Data/test-data.csv", 2000.001, 2011.8), 2
        )

if __name__ == "__main__":
    unittest.main()