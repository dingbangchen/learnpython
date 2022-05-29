import csv
import sys

csv_file = sys.argv[1]

hash_map = {}
with open(csv_file, "r") as f:
    for line in csv.reader(f):
        key = line[0]
        value = line[1]
        if key in hash_map:
            hash_map[key].append(value)
        else:
            hash_map[key] = [ value ]
