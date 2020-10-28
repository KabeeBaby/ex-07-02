fhand = open('romeo.txt')
count = 0
fwords = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word in fwords: continue
        fwords.append(word)
fwords.sort()
print(fwords)
