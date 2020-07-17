# Pass command line arguments using argparse
import argparse

parser = argparse.ArgumentParser(description='Passing command line arguments')
parser.add_argument('-f', '--file', help = 'File name')
parser.add_argument('-c', '--country', help = 'Country name')

args = parser.parse_args()

file = args.file
country = args.country

print('file is', file)
print('country is', country)

# Passing command line arguments using os.sys
import os
