# used in the pandas version
import pandas as pd

def debugger_util(lowest_temp, station_id, date):
    print("The lowest temperature recorded was ", lowest_temp)
    print("The station id that recorded the lowest temp was: ", station_id)
    print("The lowest temperature was recorded on: ", date)

# Function 1) Get lowest temp using Pandas
def get_lowest_temp_pd(file):
    data_frame = pd.read_csv(file, usecols=["station_id", "date", "temperature_c"])
    min_frame = data_frame.sort_values(by=["temperature_c"])
    station_id = min_frame.iloc[0][0]
    date = min_frame.iloc[0][1]
    lowest_temp = min_frame.iloc[0][2]
    # debug
    # debugger_util(lowest_temp, station_id, date)
    return station_id, date

"""
Uncomment below for debugging and perf timing (tests all three functions
print("Getting the station and date of the lowest possible temperature using pandas")
start_time = time.time()
get_lowest_temp_pd("Data/data.csv")
print("The first function took ", exec_time(start_time), " to execute")

print(
    "Getting the station and date of the lowest possible temperature using csv's DictReader"
)
"""