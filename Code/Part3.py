# used in the pandas version
import pandas as pd

"""
**Part 3**:

Create a function that will return the `station_id` that experienced the most amount of temperature
fluctuation for any given range of dates. I.e to get the result of 10 degrees from part 2 above, we
would expect the input dates to be `2000.001` and `2000.456`.
"""


def get_temp_flucs_date_range(csv, start_date, end_date):
    df = pd.read_csv(
        csv,
    )

    # create a deduped list of station ids
    deduped_stations = set(df["station_id"].values)

    # Select Pandas dataframe rows between two dates. We can perform this
    # using a boolean mask. Valid dates formats include
    # datetime(numpy and pandas), timestamps, or strings
    date_mask = (df["date"] > start_date) & (df["date"] <= end_date)

    # assign mask to df to return the rows with birth_date between our specified start/end dates
    df = df.loc[date_mask]

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


# Uncomment below for debugging and perf timing
"""
get_temp_flucs_date_range("Data/test-data-1.csv", 2000.001, 2011.8)
get_temp_flucs_date_range("Data/test-data-2.csv", 2000.001, 2011.8)
get_temp_flucs_date_range("Data/test-data.csv", 2000.001, 2011.8)
get_temp_flucs_date_range("Data/data.csv", 2000.001, 2011.8)
"""

# the processing Data/data.csv should output: 735181
