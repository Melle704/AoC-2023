import math

lines = open("input.txt", "r")

directions = dict()
keys = []

route = lines.readline()

# Parse the lines to a dictionary.
for line in lines:
    # Remove characters.
    for char in ['(', ')', ',']:
        line = line.replace(char, '')
    line = line.strip().split(' ')

    # Try to add the keys to the dictionary.
    try:
        directions[line[0]] = (line[2], line[3])
        if line[0][2] == 'A':
            keys.append(line[0])
    except:
        ValueError

part1 = 0
part2 = 0

# Loop through the found keys.
for current in keys:
    total = 0
    for i in range(100000):
        if current[2] == 'Z':
            # If the keys solution is ZZZ, that is the solution of part 1.
            if current == "ZZZ":
                part1 = total
            break
        char = route[i % len(route)]
        if char == 'R':
            _, current = directions[current]
            total += 1
        elif char == 'L':
            current, _ = directions[current]
            total += 1

    # Calculate the least common multiple of the current total and the new shortest path.
    if part2 != 0:
        part2 = math.lcm(part2, total)
    else:
        part2 = total

print("Part1:", part1)
print("Part2:", part2)