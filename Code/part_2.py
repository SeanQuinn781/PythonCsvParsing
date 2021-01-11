import csv
import time

"""
**Part 2**:
Create a function that returns the `station_id` that experienced the most amount of
temperature fluctuation across all dates that it reported temperatures for. For example
with the following dataset:

    station_id,     date, temperature_c
             1, 2000.001,             5
             1, 2000.123,             0
             1, 2000.456,             5
             2, 2000.001,             10

we are expecting the total fluctuation to be 10 degrees, as opposed to 0 which is the net difference
in temperature between the first and last dates.
"""

def exec_time(start):
    return time.time() - start

# returns the `station_id` that experienced the most amount of temperature fluctuation
def get_temp_flucs(csv_file):
    reader = csv.DictReader(open(csv_file), delimiter=",")
    sorted_list = sorted(reader, key=lambda row: (row["station_id"]), reverse=False)
    first_iteration = True
    last_temp = 0
    most_fluc_seen = 0
    station_with_most_flucs = 0
    cur_total_flucs = 0

    for line in sorted_list:
        date = line["date"]
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


# Uncomment below for debugging/ manual testing
"""
get_temp_flucs("Data/test-data-1.csv")
get_temp_flucs("Data/test-data-2.csv")
get_temp_flucs("Data/test-data.csv")
print("---------------------------")
start_time = time.time()
get_temp_flucs("Data/data.csv")
print("The first function took ", exec_time(start_time), " to execute")
"""


"""
Result and performance info for Data/data.csv:

Most flucs seen was:  2760.555999999999
Station with the most flucs:  735181
The first function took  17.451486825942993  to execute
"""