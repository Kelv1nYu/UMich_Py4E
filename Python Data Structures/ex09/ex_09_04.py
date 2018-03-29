#file operation and list operation and dictionary opreation

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

names = list()
counts = dict()
largestValue = None
largestName = None

for line in handle:
    if not line.startswith("From:"):
        continue
    else:
        names.append(line.split()[1])

for name in names:
    counts[name] = counts.get(name, 0) + 1

for name,count in counts.items():
    if largestValue is None or largestValue < count:
        largestName = name
        largestValue = count
        
print(largestName, largestValue)
