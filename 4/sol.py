input_file = open("input.txt", "r")

part1 = 0
data = []
orig_data = []

for i, line in enumerate(input_file):
    line = line[10:].strip().split(' | ')

    # Convert the string to simple integer arrays.
    numbers = [int(i) for i in line[0].split(' ') if i]
    winning_numbers = [int(i) for i in line[1].split(' ') if i]

    # Calculate part 1.
    amount = 0
    for num in numbers:
        if num in winning_numbers:
            amount += 1
    if amount != 0:
        part1 += 2**(amount-1)

    # Append the list of numbers to a list.
    data.append((numbers, amount, len(data)))
    orig_data.append((numbers, amount, len(data)))

# Calculate the answer of part 2.
cor = 1
for i, (numbers, amount, index) in enumerate(data):
    if i >= len(orig_data):
        cor = 0

    # Append all the new scratchcards to the list.
    for di in range(0, amount):
        if index+di+cor < len(orig_data):
            data.append(orig_data[index+di+cor])

print("Part1: ", part1)
print("Part2: ", len(data))