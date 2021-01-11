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


def get_temp_flucs_pd(csv):
    df = pd.read_csv(
        csv,
        usecols=["station_id", "temperature_c"],
    ).sort_values(by=["station_id"])

    # create a deduped list of station ids
    deduped_stations = set(df["station_id"].values)

    # track flucs per station and most overall
    station_with_most_flucs = 0
    most_fluc_seen = 0

    # iterate of deduped stations for effeciency since we can get all the temps
    # for that station in a single go using df
    for station in deduped_stations:
        # print(station)
        # get all temps recorded at the current station
        station_temps = df[df["station_id"] == station]["temperature_c"].values
        # get sum of all fluctuations at this station
        sum_of_flucs = abs(station_temps[:-1] - station_temps[1:]).sum()

        if sum_of_flucs > most_fluc_seen:
            most_fluc_seen = sum_of_flucs
            station_with_most_flucs = station

    print("Most flucs seen was ", most_fluc_seen)
    print("Station with the most flucs is ", station_with_most_flucs)
    return station_with_most_flucs


# Uncomment below for debugging/ manual testing
get_temp_flucs_pd("Data/test-data-1.csv")
get_temp_flucs_pd("Data/test-data-2.csv")
get_temp_flucs_pd("Data/test-data.csv")
get_temp_flucs_pd("Data/data.csv")
