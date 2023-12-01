input_file = open("input.txt", "r")

total = 0
arr = []

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in input_file:
    first_char = None
    last_char = None
    current_word = ""

    for char in line:
        # Check for a written out number.
        if char.isalpha():
            current_word += char
            for key in numbers:
                if key in current_word:
                    if first_char is None:
                        first_char = numbers[key]
                    else:
                        last_char = numbers[key]
                    current_word = char

        # Check for a integer.
        if char.isnumeric():
            if first_char is None:
                first_char = char
            last_char = char

    # Concatenate the first and last number.
    if last_char is not None:
        arr.append(int(first_char + last_char))
    elif first_char is not None:
        arr.append(int(first_char + first_char))

input_file.close()

print(arr)
print(sum(arr))

