#!/usr/bin/env python3
# Python script that displays a puzzle as seen in the novel "Empire of the ants"
# Usage : puzzle.py -n [number of iterations]

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--iter", required=True, help="Number of iterations")
args = parser.parse_args()

try:
    iterations = int(args.iter)
except:
    print("Invalid argument. Please input an integer.")
    exit()

numbers = [1]
buffer = "%s\n"%(numbers[0])
for _ in range(iterations):
    temp = []
    count = 0
    for i in range(len(numbers)):
        if i > 0 and numbers[i-1]!=numbers[i]:
            temp += [count, numbers[i-1]]
            buffer += "%s %s "%(count, numbers[i-1])
            count = 0
        count += 1
    temp += [count, numbers[i]]
    buffer += "%s %s\n"%(count, numbers[i])
    numbers = temp
print(buffer, end='')