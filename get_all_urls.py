'''
This program parses all the Urls from the json files.
'''
import re
import os
import sys

json_files_dir = sys.argv[1]

pattern = re.compile('clone_url*')
for root, dirs, files in os.walk(json_files_dir):
    for source_file in files:
        if source_file.endswith('.json'):
            json_file = root+'/'+source_file
            with open(json_file,'r') as f:
                for line in f:
                    match = re.search(pattern, line)
                    if match:
                        line = line.replace('\"','')
                        line = line.replace('clone_url','')
                        line = line.replace(':','')
                        line = line.replace(',','')
                        line = line.strip()
                        print(line)
                f.close()



