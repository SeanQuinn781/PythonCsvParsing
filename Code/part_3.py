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
    flucs_seen = []
    last_temp = 0
    most_fluc_seen = 0
    station_with_most_flucs = 0
    cur_total_flucs = 0

    for line in sorted_list:
        date = line["date"]
        """
        print("line is ", line)
        print('start date is ', start_date)
        print('cur date is ', date)
        print('end date is ', end_date)  # and line['date'] < end_date
        print('date occurs after start date: ', (date > start_date))
        print('date occurs before end date: ', date < end_date)
        """
        if date >= start_date and date <= end_date:
            temp = float(line["temperature_c"])

            # if its the first iteration we need to initialize some variables
            if first_iteration:
                last_temp = temp
                first_iteration = False
                cur_station = line["station_id"]

            # if the station changes we need to reset some variables
            if cur_station != line["station_id"]:

                # find the total flucs between all temps at cur_station
                # iterate over every temperature finding the fluctuation between
                # consecutive temps, adding to the total fluctuation with each item
                # for first, second in zip(flucs_seen,flucs_seen[1:]):
                #    cur_total_flucs += abs(first - second)
                # print("flucs seen for station", cur_station, " is ", cur_total_flucs)
                if cur_total_flucs > most_fluc_seen:
                    most_fluc_seen = cur_total_flucs
                    station_with_most_flucs = cur_station

                # reset current_station until next time station updates
                cur_station = line["station_id"]
                # update last_temp with current temp for new station
                last_temp = temp
                # reset flucs_seen for the new station
                flucs_seen = []
                flucs_seen.append(temp)
                # reset cur total flucs
                cur_total_flucs = 0

            else:
                flucs_seen.append(temp)

                # for first, second in zip(flucs_seen,flucs_seen[1:]):
                #    cur_total_flucs += abs(first - second)
                print("flucs seen for station", cur_station, " is ", cur_total_flucs)

                if cur_total_flucs > most_fluc_seen:
                    most_fluc_seen = cur_total_flucs
                    station_with_most_flucs = cur_station




    print("Most flucs seen was: ", most_fluc_seen)
    print("Station with the most flucs: ", station_with_most_flucs)
    return station_with_most_flucs


# Uncomment below for debugging and perf timing
"""

get_temp_flucs_date_range("Data/test-data-1.csv", "2000.001", "2011.8")
print("---------------------------")
get_temp_flucs_date_range("Data/test-data-2.csv", "2000.001", "2011.8")
print("---------------------------")
get_temp_flucs_date_range("Data/test-data.csv", "2000.001", "2012.002")
"""
start_time = time.time()
print("---------------------------")
get_temp_flucs_date_range("Data/test-data.csv", "2000.001", "2011.8")
print("The first function took ", exec_time(start_time), " to execute")

"""
Result and performance info:

Most flucs seen was:  38.601
Station with the most flucs:  659516
The first function took  26.598039388656616  to execute

"""
# the processing Data/data.csv should output: 735181
