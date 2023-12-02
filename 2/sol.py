input_file = open("input.txt", "r")

colors = ["red", "green", "blue"]
values = []

part1 = 0
part2 = []

for i, line in enumerate(input_file):
    # Find the largest value for each color, and append to the array.
    for color in colors:
        curr_value = 0
        for i2 in range(len(line)):
            if line.startswith(color, i2):
                if int(line[i2 - 3] + line[i2 - 2]) > curr_value:
                    curr_value = int(line[i2 - 3] + line[i2 - 2])
        values.append(curr_value)

    # Part 1
    if values[i*3] < 13 and values[i*3+1] < 14 and values[i*3+2] < 15:
        part1 += i+1

    # Part 2
    part2.append(values[i*3] * values[i*3+1] * values[i*3+2])

print(values)
print("part1 ", part1)
print("part2 ", sum(part2))