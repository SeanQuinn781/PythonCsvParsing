import csv

# used for perf timing
import time

"""
**Part 3**:

Create a function that will return the `station_id` that experienced the most amount of temperature
fluctuation for any given range of dates. I.e to get the result of 10 degrees from part 2 above, we
would expect the input dates to be `2000.001` and `2000.456`.

Note: this is faster but requires an extra import
import itertools

for first, second in itertools.izip(l, l[1:]):
"""


def exec_time(start):
    return time.time() - start


def get_temp_flucs_date_range(csv_file, start_date, end_date):

    reader = csv.DictReader(open(csv_file), delimiter=",")
    sorted_list = sorted(reader, key=lambda row: (row["station_id"]), reverse=False)
    first_iteration = True
    last_temp = 0
    most_fluc_seen = 0
    station_with_most_flucs = 0
    cur_total_flucs = 0


    for line in sorted_list:
        date = line["date"]

        if date >= start_date and date <= end_date:
            temp = float(line["temperature_c"])

            # if its the first iteration we need to initialize some variables
            if first_iteration:
                last_temp = temp
                first_iteration = False
                cur_station = line["station_id"]

            # if the station changes we need to reset some variables
            if cur_station != line["station_id"]:
                if cur_total_flucs > most_fluc_seen:
                    most_fluc_seen = cur_total_flucs
                    station_with_most_flucs = cur_station

                # reset current_station until next time station updates
                cur_station = line["station_id"]

                # reset cur total flucs
                cur_total_flucs = 0

            else:
                cur_fluc = abs(last_temp - temp)
                cur_total_flucs += cur_fluc
                if cur_total_flucs > most_fluc_seen:
                    most_fluc_seen = cur_total_flucs
                    station_with_most_flucs = cur_station

            last_temp = temp

    print("Most flucs seen was: ", most_fluc_seen)
    print("Station with the most flucs: ", station_with_most_flucs)
    return station_with_most_flucs


# Uncomment below for debugging and perf timing

get_temp_flucs_date_range("Data/test-data-1.csv", "2000.001", "2011.8")
print("---------------------------")
get_temp_flucs_date_range("Data/test-data-2.csv", "2000.001", "2011.8")
print("---------------------------")
get_temp_flucs_date_range("Data/test-data.csv", "2000.001", "2012.002")
print("---------------------------")
start_time = time.time()
get_temp_flucs_date_range("Data/data.csv", "2000.001", "2011.8")
print("The first function took ", exec_time(start_time), " to execute")

"""
Result and performance info for Data/data.csv:

Most flucs seen was:  1610.3680000000002
Station with the most flucs:  735181
The first function took  17.110  to execute
"""
