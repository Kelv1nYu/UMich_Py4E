#file operation

fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
        #print(line)
        words = line.split()[1]
        print(words)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
