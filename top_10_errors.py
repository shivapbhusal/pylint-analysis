'''
Finds top 10 errors and their percentage
'''
import sys


def get_k_top_values(error_dict,k=10):
    for key, value in sorted(error_dict.items(), key = lambda item: item[1], reverse=True):
        print("%s: %s" % (key, value))


result_file = sys.argv[1]
error_dict = {}

total = 0
with open(result_file,'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(':')
        error_type = line[0]
        frequency = line[1]
        total = total+int(frequency)
        if error_type not in error_dict:
            error_dict[error_type] = int(frequency)
    f.close()

for error in error_dict:
    error_dict[error] = float(error_dict[error])*100/total

get_k_top_values(error_dict)



