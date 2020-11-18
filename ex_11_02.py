import re
fhandle= open("mbox-short.txt")
sum = 0
count = 0
for line in fhandle:
    x = re.findall("^New Revision: ([0-9]+)", line)
    for n in x:
        n = int(n)
        sum = sum + n
        count = count + 1
average = sum / count



print("New Revision:", average)
