'''
This program analyzes common errors in Python repos analysed.
'''
import re

pattern = re.compile(r'C[0-9]|E[0-9]|F[0-9]|I[0-9]|R[0-9]|W[0-9]|RP[0-9]')
errors = re.findall(pattern, 'TESTC00RP000TEST')

print(errors)



