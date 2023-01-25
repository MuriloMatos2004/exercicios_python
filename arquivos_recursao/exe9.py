arq = open("CJ-021122.csv", "r")
temp_min = []
temp_max = []

while True:
    line = arq.readline()
    if not line: break

    line = line.split(',')
    temp_max.append(line[3])
    temp_min.append(line[4])

temp_max.pop(0)
temp_min.pop(0)

max = temp_max[0]
for i in temp_max:
    if float(i) > float(max):
        max = i

min = temp_min[0]
for j in temp_min:
    if float(j) < float(min):
        min = j

print("max: {ma} min: {mi}".format(ma = max, mi = min))

arq.close()