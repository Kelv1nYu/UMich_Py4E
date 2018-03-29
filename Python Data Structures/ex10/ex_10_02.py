 #file opreation and list opreation and dictionary opreation and tuple
    
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
