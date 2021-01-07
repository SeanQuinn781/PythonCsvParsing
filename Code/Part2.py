# used in the pandas version
import pandas as pd

"""
**Part 2**:
Create a function that returns the `station_id` that experienced the most amount of temperature
fluctuation across all dates that it reported temperatures for. For example with the following dataset:

    station_id,     date, temperature_c
             1, 2000.001,             5
             1, 2000.123,             0
             1, 2000.456,             5
             2, 2000.001,             10

we are expecting the total fluctuation to be 10 degrees, as opposed to 0 which is the net difference
in temperature between the first and last dates.
"""

# returns the `station_id` that experienced the most amount of temperature fluctuation
def get_temp_flucs(csv):
    # Disregard the unneeded date column in our dataframe, sort the weather data by station_id
    df = pd.read_csv(csv, usecols=["station_id", "temperature_c"]).sort_values(
        by=["station_id"]
    )

    # Prev row temp is used to find the fluctuation between the prev row's temp and current
    station_with_most_flucs = 0
    most_fluc_seen = 0
    fluc_per_station = 0
    # init flag so we know its the first loop and need to init vars
    first_iteration = True

    for item, row in df.iterrows():
        # Assign row values (station and temperature) to variables for tracking fluctuations
        row_station = row[0]
        cur_row_temp = row[1]

        # On first loop iteration there was no last row temperature so init last_row_temp to current_row_temp, and
        # there was no previous row station so set previous row station id to current row station id
        if first_iteration:
            cur_row_station = row_station
            prev_row_temp = cur_row_temp

            # initialization is complete, set first_iteration to false
            first_iteration = False

        # Else if we are still on the same station then track fluctuations seen on this station so far
        elif cur_row_station == row_station:
            # find the fluctuation between the prev temp and current
            curr_fluc = abs(prev_row_temp - cur_row_temp)

            # add the fluc to the total fluc count for this station
            fluc_per_station += curr_fluc

            # cur_row_temp is updated in each loop so save it in prev_row_temp since we are done tracking data
            prev_row_temp = cur_row_temp

            # if current_temp_flucs_seen > most_flucs_seen then assign current to most
            if fluc_per_station > most_fluc_seen:
                station_with_most_flucs = cur_row_station
                most_fluc_seen = fluc_per_station

        # if its not the first iteration and cur_row_station != row_station we must iterating a new station's data
        # reset relevant vars. The stations temp data is sorted by station_id so we can use a single iteration
        else:
            # re-init vars for tracking temp and station
            cur_row_station = row_station
            prev_row_temp = cur_row_temp
            fluc_per_station = 0

    print("The station with the most fluctuations is ", station_with_most_flucs)
    print("The most flucs seen is ", most_fluc_seen)
    return station_with_most_flucs


# Uncomment below for debugging/ manual testing
"""
get_temp_flucs("Data/test-data-1.csv")
get_temp_flucs("Data/test-data-2.csv")
get_temp_flucs("Data/test-data.csv")
get_temp_flucs("Data/data.csv")
"""
