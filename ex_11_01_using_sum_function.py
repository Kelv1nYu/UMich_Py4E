# using the fucntion sum() to get the sum of the list

import re

filename = input("File name:")
if len(filename) < 1: filename = "regex_sum_55433.txt"

nums = list()
counts = dict()

with open(filename) as f:
	for line in f:
		line = line.rstrip()
		tmpnums = re.findall('[0-9]+', line)
		for tmpnum in tmpnums:
			nums.append(tmpnum)

# change the list of strings into list of integer, because the sum function cannot sum up the strings

for i in range(len(nums)):
	nums[i] = int(nums[i])

tot = sum(nums)

print(tot)
