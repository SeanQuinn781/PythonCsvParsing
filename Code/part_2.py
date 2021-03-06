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
    # make sure to convert station_id to int before sorting for correct results
    sorted_list = sorted(reader, key=lambda row: (int(row["station_id"])), reverse=False)
    first_iteration = True
    last_temp = 0
    most_fluc_seen = 0
    station_with_most_flucs = 0
    cur_total_flucs = 0
    cur_station = 0

    for line in sorted_list:
        temp = float(line["temperature_c"])
        station = int(line["station_id"])

        # if its the first iteration we need to initialize some variables
        if first_iteration:
            last_temp = temp
            first_iteration = False
            cur_station = station

        # if the station changes we need to reset some variables
        if cur_station != station:
            if cur_total_flucs > most_fluc_seen:
                most_fluc_seen = cur_total_flucs
                station_with_most_flucs = cur_station

            # reset current_station until next time station updates
            cur_station = station

            # reset cur total flucs
            cur_total_flucs = 0

        else:
            cur_fluc = abs(last_temp - temp)
            # make sure to convert cur_fluc (float) to int when tracking most fluctuations
            cur_total_flucs += int(cur_fluc)
            last_temp = temp

            if cur_total_flucs > most_fluc_seen:
                most_fluc_seen = cur_total_flucs
                station_with_most_flucs = cur_station

    print("Station with the most flucs: ", station_with_most_flucs)
    print("Most flucs seen: ", most_fluc_seen)
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
Station with the most flucs:  758064
Most flucs seen:  2532
The first function took  18.426657915115356  to execute

"""