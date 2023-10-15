# Assignment 2 created by Joseph Oppong

## Introdution
In this assignment, we are asked to calculate descriptive statistics for numbers found in columns of a given input file. Descriptive statistics is a branch of statistics that deals with the summarization, organization, and interpretation of data to gain insights and describe its main characteristics. Descriptive statistics are used to provide a concise overview of a dataset's characteristics, making it easier to understand its distribution and properties. They are essential tools in data analysis and decision-making processes across various fields, such as science, business, social sciences, and more.

In descriptive statistics, we calculate:
- Average
- Maximum
- minimum
- variance
- standard deviation
- Median

## Here is a step-by-step overview of the program:
1.Import required modules (sys, collections, math)

2. Define get_stats() function that takes filename and column number as arguments

3. Initialize empty list to store numbers

4. Open file and loop through each line:
 - Split line on tabs
 - Try to convert specified column to float
 - Append to numbers list if successful
 - Print error message on failure
5. After loop, check if numbers list is empty
 - If so, print error message and return
6. Calculate statistics:
 - Count, valid count
 - Sum, min, max for average, min, max
 - Variance and standard deviation
 - Median
7. Store stats in a dictionary
8. Print column number
9. Print each statistic nicely formatted:
 - Use format() or f-strings to align decimals
10. Call get_stats() function with filename and column number from command line arguments
