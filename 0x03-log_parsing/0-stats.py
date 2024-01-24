#!/usr/bin/python3
"""
script that reads stdin line by line
and computes metrics based on inputs
"""


import sys

# Initialize a dict to store counts for each status code
# The keys are status codes and initially set to 0
status_code_counts = {'200': 0, '301': 0, '400': 0,
                      '401': 0, '403': 0, '404': 0,
                      '405': 0, '500': 0}
# Initialize variables to keep track
# of the total file size and a line counter
total_size = 0
line_counter = 0

try:
    # Loop through each line of input from the stdin
    for line in sys.stdin:
        # Split the line into words
        words = line.split(" ")
        # Check if the line has more than 4 words
        if len(words) > 4:
            status_code = words[-2]
            size = int(words[-1])
            # Update count for status code in dict
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1
            # Update the total file size and line counter
            total_size += size
            line_counter += 1
        # Check if 10 lines have been processed
        if line_counter == 10:
            line_counter = 0  # Reset the line counter
            print('File size: {}'.format(total_size))
            # Print the counts of status code in sorted order
            for key, value in sorted(status_code_counts.items()): 
                if value != 0:
                    print('{}: {}'.format(key, value)) 
except Exception as error:
    # Catch and ignore exceptions
    pass

finally:
    print('File size: {}'.format(total_size))
    # Print the counts of each status code in sorted order
    for key, value in sorted(status_code_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

               
