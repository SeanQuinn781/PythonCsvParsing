import csv

# used for perf timing
import time

"""
**Part 3**:

Create a function that will return the `station_id` that experienced the most amount of temperature
fluctuation for any given range of dates. I.e to get the result of 10 degrees from part 2 above, we
would expect the input dates to be `2000.001` and `2000.456`.
"""


def exec_time(start):
    return time.time() - start


def get_temp_flucs_date_range(csv_file, start_date, end_date):

    reader = csv.DictReader(open(csv_file), delimiter=",")
    sorted_list = sorted(reader, key=lambda row: (row["station_id"]), reverse=False)
    first_iteration = True
    flucs_seen = 0
    last_temp = 0
    most_fluc_seen = 0
    station_with_most_flucs = 0

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
            print("station is ", line["station_id"])
            print("cur_station is ", cur_station)
            if cur_station != line["station_id"]:
                print("cur station not equal to station")
                # reset current_station until next time station updates
                cur_station = line["station_id"]
                # update last_temp with current temp for new station
                last_temp = temp
                # reset flucs_seen for the new station
                flucs_seen = 0
                print("now station is ", line["station_id"])
                print("now cur station is ", cur_station)

            # get current flucs
            cur_flucs = abs(last_temp - temp)
            flucs_seen = flucs_seen + cur_flucs

            if flucs_seen > most_fluc_seen:
                print("flucs seen ", flucs_seen, "is bigger than most flucs seen ",most_fluc_seen )
                most_fluc_seen = flucs_seen
                station_with_most_flucs = cur_station
        else:
            break

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
