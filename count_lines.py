'''
This program searches for the Python files in a directory, 
and gets the number of lines of code and sums everything up. 
Basically, it finds out the number of lines of Python code in a directory.
'''
import sys
import io
import os

def count_lines(file_path):
    count = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                count += 1
        return count
    except:
        return 0
        
data_path = sys.argv[1]

total_count = 0
for root, dirs, files in os.walk(data_path):
    for source_file in files:
        if source_file.endswith('.py'):
            file_path = root+'/'+source_file
            print(file_path)
            print(count_lines(file_path))
            total_count += count_lines(file_path)

print(total_count)
