'''
Day 1 of AOC - Part 1 - trebuchet
'''
import re

with open("input.txt") as input:
    content = input.readlines()
    content = [line.strip() for line in content]

    total_calibration = 0
    for line in content:
        only_nums = re.sub("\D+", "",line)

        total_calibration += int(only_nums[0]+only_nums[-1])

    print(total_calibration)    