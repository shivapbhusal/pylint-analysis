'''
This program analyzes common errors in Python repos analysed.
'''
import re
import sys


error_dict = dict()

result_file = sys.argv[1]
pattern = re.compile(r'C[0-9]{4}|E[0-9]{4}|F[0-9]{4}|I[0-9]{4}|R[0-9]{4}|W[0-9]{4}|RP[0-9]{4}')

with open(result_file, 'r') as f:
    for line in f:
        errors = re.findall(pattern, line)
        if errors:
            for error in errors:
                error = error.strip()
                if error in error_dict:
                    error_dict[error]+=1
                else:
                    error_dict[error]=1
    f.close()

for error_type in error_dict:
    print(error_type +':' + str(error_dict[error_type]))



