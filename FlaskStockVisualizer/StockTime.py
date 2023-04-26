from datetime import datetime
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# This function asks the user for the time series option and returns the user's input.

def get_time_series_option():
    while True:
        print("Enter the time series option:")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        time_series_option = input("Option: ")
        if time_series_option not in ["1", "2", "3", "4"]:
            print("Invalid option. Please enter either 1, 2, 3, or 4.")
        else:
            return int(time_series_option)

# This function asks the user for the start date and returns the user's input.

def get_start_date():
    while True:
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            return start_date
        except:
            print("Error: incorrect input. Please enter input as (YYYY-MM-DD)")

# This function asks the user for the end date and validates that the end date is not before the start date. It returns the user's input if it is valid.

def get_end_date(start_date):
    # while True:
    #     end_date_str = input("Enter the end date (YYYY-MM-DD): ")
    #     try:
    #         end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    #         continue
    #     except:
    #         print("Error: incorrect input. Please enter input as (YYYY-MM-DD)")
    while True:
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            start_timestamp = int(pd.Timestamp(start_date).timestamp())
            end_timestamp = int(pd.Timestamp(end_date).timestamp())
            if end_timestamp < start_timestamp:
                raise ValueError("End date must be after start date.")
        except ValueError as e:
            print("Invalid date input:", e)
            continue
        except:
            print("Error: incorrect input. Please enter input as (YYYY-MM-DD)")
            continue
        return end_date

def get_start_time():
    while True:
        start_time_str = input("Enter a time (HH:MM:SS): ")
        try:
            start_time = datetime.strptime(start_time_str, "%H:%M:%S").time()
            return start_time
        except:
            print("Error: incorrect input. Please enter input as (H:M:S)")

    
