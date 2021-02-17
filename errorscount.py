import os
from os import walk

dir_path = os.path.dirname(os.path.realpath(__file__))

f = []
for (dirpath, dirnames, filenames) in walk(dir_path):
    f.extend(filenames)

counters = {}

for file in f:
    if not os.path.splitext(file)[1] == ".log":
        continue

    with open(file) as f:
        content = f.readlines()

    for entry in content:
        parts = entry.split("|")

        date = parts[0][1:11]

        if not date in counters:
            counters[date] = 0

        if "ERROR" in parts[1]:
            counters[date] += 1

        if "FATAL" in parts[1]:
            counters[date] += 1

        if "CRITICAL" in parts[1]:
            counters[date] += 1

for k, v in counters.items():
    print(k + " = " + str(v))
