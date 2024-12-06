

file = open("input.txt", "r")
col1 = []
col2 = []
for i in file.readlines():
    list = " ".join(i.split()).split()
    col1.append(int(list[0]))
    col2.append(int(list[1]))

col1.sort()
col2.sort()

pairs = []
for i in range(0, len(col1)):
    pairs.append((col1[i], col2[i]))

distanceSum = 0
for i in pairs:
    distance = abs(i[0] - i[1])
    # print(i)
    distanceSum += distance
print(len(pairs))
print(distanceSum)