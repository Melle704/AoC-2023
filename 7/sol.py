from collections import Counter

lines = open("input.txt", "r")

scores = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

scores["J"] = 0

hand_bids = []

for hand in lines:
    hand, bid = hand.split()
    hand_bids.append((hand, int(bid)))

arr = []

for hand, bid in hand_bids:
    char_counts = Counter(hand)

    # Handle jokers.
    joker_count = 0
    if "J" in char_counts:
        joker_count = char_counts["J"]
        char_counts["J"] = 0

    # Find the most common character and its count.
    most_common_char = ""
    most_common_count = 0
    for char, count in char_counts.items():
        if count > most_common_count:
            most_common_char = char
            most_common_count = count

    if most_common_count == 1:
        rank = 7
    elif most_common_count == 2:
        if 4 in char_counts.values():
            rank = 6
        elif 3 in char_counts.values():
            rank = 5
        else:
            rank = 4

    elif 3 in char_counts.values():
        rank = 3
    elif 2 in char_counts.values():
        rank = 2
    else:
        rank = 1

    arr.append((rank, bid))

# Sort the list of hands
in_order = sorted(arr, key=lambda winning: winning[0])

part2 = 0
rank = 1
for hand, bid in in_order:
    part2 += bid * rank
    rank += 1

print("Part2: ", part2)