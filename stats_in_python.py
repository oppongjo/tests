import sys
from collections import defaultdict
from math import sqrt
import math


def get_stats(filename, column_index):
    numbers = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            try:
                fields = line.split('\t')
                num = float(fields[column_index])
                numbers.append(num)
            except (IndexError, ValueError):
                print(f"Skipping line: could not convert to float: {line}")

    if len(numbers) == 0:
        print(f"Error: There were no valid numbers in column {column_index} in file: {filename}")
        return

    count = len(numbers)
    valid_count = len([n for n in numbers if not math.isnan(n)])
    numbers = [n for n in numbers if not math.isnan(n)]

    stats = defaultdict(float)
    stats['Count'] = count
    stats['ValidNum'] = valid_count

    if valid_count > 0:
        stats['Average'] = sum(numbers) / valid_count
        stats['Maximum'] = max(numbers)
        stats['Minimum'] = min(numbers)
        variance = sum([(n - stats['Average']) ** 2 for n in numbers]) / (valid_count - 1)
        stats['Variance'] = variance
        stats['Std Dev'] = sqrt(variance)
        numbers.sort()
        stats['Median'] = numbers[valid_count // 2] 
        if valid_count % 2 == 1 
        else (numbers[valid_count // 2 - 1] + numbers[valid_count // 2]) / 2

    print(f"Column: {column_index}")

    for k, v in stats.items():
        print(f"{k:8} = {v:10.3f}")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python stats_in_python.py <filename> <column>")
        sys.exit()

    filename = sys.argv[1]
    column_index = int(sys.argv[2]) - 1

    get_stats(filename, column_index)
