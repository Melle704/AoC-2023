input_file = open('input.txt').read()

arr = []
for line in input_file.split('\n'):
    if line.strip():
        arr.append([int(i) for i in line.split()])

# Recursive next list.
def next(arr):
    if sum(i != 0 for i in arr) == 0:
        return 0

    m = []
    for i in range(len(arr) - 1):
        m.append(arr[i + 1] - arr[i])

    return arr[-1] + next(m)

part1 = 0
for i in arr:
    part1 += next(i)
print("Part1:", part1)

part2 = 0
for i in arr:
    reversed_i = i[::-1]
    part2 += next(reversed_i)
print("Part2:", part2)
