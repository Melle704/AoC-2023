input_file = open("input.txt", "r")

time = [int(value) for value in input_file.readline().strip().split(" ")[1:] if value]
time_value = ""
for elem in time:
    time_value += str(elem)

dist = [int(value) for value in input_file.readline().strip().split(" ")[1:] if value]
dist_value = ""
for elem in dist:
    dist_value += str(elem)

part1 = 0
part2 = 0

for i, elem in enumerate(time):
    if elem:
        record = dist[i]
        total = 0
        for i2 in range(0,time[i]):
            if (time[i] - i2) * i2 > record:
                total += 1
                part2 += 1

        if part1 == 0:
            part1 = total
        else:
            part1 = part1 * total

record = int(dist_value)
for i in range(0,int(time_value)):
    if (int(time_value) - i) * i > record:
        part2 += 1

print("Part1: ", part1)
print("Part2: ", part2)
