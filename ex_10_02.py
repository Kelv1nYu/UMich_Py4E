'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
hours = list()

for line in handle:
    if not line.startswith("From"):
        continue
    else:
        if not line.startswith("From:"):
            time = line.split()[5]
            pos = time.find(":")
            hours.append(time[:pos])

for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1

tmps = list()

for k, v in counts.items():
    tmp = (k, v)
    tmps.append(tmp)

tmps = sorted(tmps)
            
for k, v in tmps:
    print(k, v)

#print(sorted([(k,v) for k,v in counts.items()])) # the simple version of sort and print
