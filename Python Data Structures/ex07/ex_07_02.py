# file operation
# Use the file name mbox-short.txt as the file name

count = 0
tot = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find('.')
    num = line[pos - 1:]
    tot = tot + float(num)
print("Average spam confidence:", tot / count)
