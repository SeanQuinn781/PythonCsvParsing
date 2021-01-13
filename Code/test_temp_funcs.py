import unittest
from part_1 import get_lowest_temp, get_lowest_temp_slowest
from part_2 import get_temp_flucs
from part_3 import get_temp_flucs_date_range

# Tests all (non-pandas) functions using test data
print("------------------------------------------")
print("Testing non-pandas temperature functions")

class TestTempFuncs(unittest.TestCase):

    # Test functions in part 1 (tests 3 different functions with 3 different data sets)
    def test_get_lowest_temp(self):
        self.assertEqual(get_lowest_temp("Data/test-data-1.csv"), ('68', '2000.375'))

        self.assertEqual(
            get_lowest_temp("Data/test-data-2.csv"), ("68", "2000.375")
        )

        self.assertEqual(
            get_lowest_temp("Data/test-data.csv"), ("1", "2000.375")
        )

    # Test functions in part 2
    def test_get_temp_flucs(self):
        self.assertEqual(get_temp_flucs("Data/test-data-1.csv"), 865329)
        self.assertEqual(get_temp_flucs("Data/test-data-2.csv"), 565329)
        self.assertEqual(get_temp_flucs("Data/test-data.csv"), 1)


    # Test function in part 3
    def test_get_temp_flucs_date_range(self):
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data-1.csv", '2000.001', '2011.8'), '865329'
        )
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data-2.csv", '2000.001', '2011.8'), '420000'
        )
        self.assertEqual(
            get_temp_flucs_date_range("Data/test-data.csv", '2000.001', '2011.8'), '2'
        )



if __name__ == "__main__":
    unittest.main()

# takes a while to execute so moved into test_full_data.py
# self.assertEqual(get_lowest_temp("Data/data.csv"), ('676223', '2010.542'))
# self.assertEqual(get_lowest_temp_pd("Data/data.csv"), (676223.0, 2010.542))

# takes a while to execute so moved into test_full_data.py
# self.assertEqual(get_temp_flucs_pd("Data/data.csv"), 757524)

# takes a while to execute so moved into test_full_data.py
# self.assertEqual(
#    get_temp_flucs_date_range("Data/data.csv", '2000.001', '2011.8'), '735181'
# )
