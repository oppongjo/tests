import sys
from collections import defaultdict
import math
from math import sqrt
"""Descriptive statistics is a branch of statistics that deals with the summarization, organization, and interpretation of data to gain insights and describe its main characteristics."""

# Define get_stats() function that takes filename and column number as arguments
def get_stats(filename, column_index):
    numbers = []   # empty list to store numbers

    with open(filename, 'r') as f:  # Open file and loop through each line
        for line in f:
            line = line.strip()

            try:
                fields = line.split('\t') # Split line on tabs 
                num = float(fields[column_index])
                numbers.append(num)
            except (IndexError, ValueError):
                print(f"Skipping line: could not convert to float: {line}")  # Try to convert specified column to float  

    if len(numbers) == 0:  # check if numbers list is empty
        print(f"Error: There were no valid numbers in column {column_index} in file: {filename}")
        return

    count = len(numbers)
    valid_count = len([n for n in numbers if not math.isnan(n)])
    numbers = [n for n in numbers if not math.isnan(n)]

    stats = defaultdict(float)
    stats['Count'] = count
    stats['ValidNum'] = valid_count

    if valid_count > 0:
        stats['Average'] = sum(numbers) / valid_count  # average or mean calculation
        stats['Maximum'] = max(numbers) # maximum in the row
        stats['Minimum'] = min(numbers) # minimum in the row
        variance = sum([(n - stats['Average'])**2 for n in numbers]) / (valid_count - 1)
        stats['Variance'] = variance   # calculate variance from square 
        stats['Std Dev'] = sqrt(variance) # standard deviation calculation 
        numbers.sort() # sort the data for median
        # if length of data is even
        stats['Median'] = numbers[valid_count // 2] if valid_count % 2 == 1 else (numbers[valid_count // 2 - 1] +
                                                                                  numbers[valid_count // 2]) / 2

    print(f"Column: {column_index}")  # printing statements

    for k, v in stats.items():
        print(f"{k:8} = {v:10.3f}")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python stats_in_python.py <filename> <column>")
        sys.exit()

    filename = sys.argv[1]
    column_index = int(sys.argv[2]) - 1

    get_stats(filename, column_index) # Call get_stats() function with filename and column number from command line arguments
