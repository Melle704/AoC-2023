input_file = open("input.txt", "r")

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

gears = {}

# Set the text file in a 2d array.
data = []
for line in input_file:
    data.append(line.strip())

# Loop through all the characters in the 2d array.
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '*':
            # Loop through the directions.
            for direction in directions:
                dx, dy = direction
                if data[i+dx][j+dy].isnumeric():
                    # Find the last number of the current continues number.
                    length = 0
                    while j + dy + length < len(line) and data[i + dx][j + dy + length].isnumeric():
                        length += 1
                    length -= 1

                    # Loop through the continues number and concat the individual numbers.
                    temp = ""
                    while data[i + dx][j + dy + length].isnumeric():
                        temp = (data[i + dx][j + dy + length]) + temp
                        length -= 1

                    # Add the coordinates of the last element and integer value to the set.
                    if (i, j) not in gears:
                        gears[(i, j)] = set()
                    gears[(i, j)].add(int(temp))

part2 = 0
for key, values in gears.items():
    if len(values) == 2:
        value1, value2 = values
        part2 += value1 * value2
print(part2)
