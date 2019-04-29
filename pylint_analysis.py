'''
This program takes a directory with Python source code as an input, runs Pylint on that directory,
and finally collects the list of most frequent errors.
'''
import sys
import io
import os
from pylint import epylint as lint

def run_pylint(file_path):
    pylint_stdout, pylint_stderr = lint.py_run(file_path, return_std=True)
    return pylint_stdout

data_path = sys.argv[1]

for root, dirs, files in os.walk(data_path):
    for source_file in files:
        if source_file.endswith('.py'):
            file_path = root+'/'+source_file
            result = run_pylint(file_path)
            print(result.getvalue())


