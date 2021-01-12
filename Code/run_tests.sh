#!/bin/sh
# shell script to run all tests in one go
python3 -m unittest test_temp_funcs.py
python3 -m unittest test_temp_funcs_pandas.py
python3 -m unittest test_full_data.py
