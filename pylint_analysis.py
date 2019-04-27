'''
This program takes a directory with Python source code as an input, runs Pylint on that directory,
and finally collects the list of most frequent errors.
'''
import sys
import io
import os
from pylint import epylint as lint

data_path = sys.argv[1]
#result_file = sys.argv[2]

pylint_stdout, pylint_stderr = lint.py_run(data_path, return_std=True)

for root, dirs, files in os.walk(data_path):
    for source_file in files:
        if source_file.endswith('.py'):
            file_path = root+'/'+source_file
            print(pylint_stdout.getvalue())
            #with open(result_file, 'a') as f:
    #f.write(pylint_stdout.getvalue())
    #f.close()
    #print(pylint_stdout.getvalue())


