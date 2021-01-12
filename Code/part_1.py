import csv

# used for perf timing
import time

"""
**Part 1**:
Create a function that when called returns the station_id, and date pair that reported the lowest temperature. 
If a tie occurs simply return one pair at random.
"""

# Function 1 Getting the lowest temp using the python3 module csv (with no additional libraries)
def get_lowest_temp(file):
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # initialize highest temp to the lowest possible temperature
        highest_temp_poss = 47
        # initilaize lowest temp to the highest possible temperature
        lowest_temp = highest_temp_poss

        for line in csv_reader:
            cur_temp = float(line["temperature_c"])
            if cur_temp < lowest_temp:
                lowest_temp = cur_temp
                station_id = line["station_id"]
                date = line["date"]
        # debug
        # debugger_util(lowest_temp, station_id, date)
    return station_id, date


def get_lowest_temp_slowest(file):
    reader = csv.DictReader(open(file, "r"))
    result = sorted(reader, key=lambda d: float(d["temperature_c"]))
    station_id = result[0]["station_id"]
    date = result[0]["date"]
    lowest_temp = result[0]["temperature_c"]
    # debug
    debugger_util(lowest_temp, station_id, date)
    return station_id, date


def debugger_util(lowest_temp, station_id, date):
    print("The lowest temperature recorded was ", lowest_temp)
    print("The station id that recorded the lowest temp was: ", station_id)
    print("The lowest temperature was recorded on: ", date)


def exec_time(start):
    exec_time = time.time() - start
    return exec_time


"""
start_time = time.time()
get_lowest_temp("Data/test-data.csv")
print("The second function took ", exec_time(start_time), " to execute")

print(
    "Getting the station and date of the lowest possible temperature "
    "using csv's DictReader and sorting data"
)
start_time_3 = time.time()
get_lowest_temp_slowest("Data/test-data-2.csv")
print("The third function took ", exec_time(start_time_3), " to execute")
"""
