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

for num in nums:
	counts[num] = counts.get(num, 0) + 1

tot = 0

for k, v in counts.items():
	tot = tot + int(k)*v

print(tot)
