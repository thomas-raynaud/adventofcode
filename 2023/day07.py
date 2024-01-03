order = [ "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]
hands_score = []

for line in open("input_d07"):
    hand, bid = line.rstrip().split(" ")
    hand = list(hand)
    bid = int(bid)

    hand_sorted = hand.copy()
    is_hand_sorted = False
    while not is_hand_sorted:
        is_hand_sorted = True
        for i in range(1, len(hand_sorted)):
            if order.index(hand_sorted[i - 1]) > order.index(hand_sorted[i]):
                hand_sorted[i - 1], hand_sorted[i] = hand_sorted[i], hand_sorted[i - 1]
                is_hand_sorted = False

    prev_x = hand_sorted[0]
    occurences = []
    curr_occurence = 1
    for x in hand_sorted[1:]:
        if prev_x == x:
            curr_occurence += 1
        else:
            occurences.append(curr_occurence)
            curr_occurence = 1
        prev_x = x
    occurences.append(curr_occurence)

    score = 0
    if len(occurences) == 1:
        # Five of a kind
        score = 1
    elif len(occurences) == 2:
        if 4 in occurences:
            # Four of a kind
            score = 2
        else:
            # Full house
            score = 3
    elif len(occurences) == 3:
        if 3 in occurences:
            # Three of a kind
            score = 4
        else:
            # Two pair
            score = 5
    elif len(occurences) == 4:
        # One pair
        score = 6
    else:
        # High card
        score = 7
    hands_score.append([ ''.join(hand), score, bid ])

are_hands_sorted = False
while not are_hands_sorted:
    are_hands_sorted = True
    for i in range(1, len(hands_score)):
        if hands_score[i - 1][1] < hands_score[i][1]:
            hands_score[i - 1], hands_score[i] = hands_score[i], hands_score[i - 1]
            are_hands_sorted = False
        elif hands_score[i - 1][1] == hands_score[i][1]:
            for a, b in zip(list(hands_score[i - 1][0]), list(hands_score[i][0])):
                if order.index(a) == order.index(b):
                    continue
                else:
                    if order.index(a) < order.index(b):
                        hands_score[i - 1], hands_score[i] = hands_score[i], hands_score[i - 1]
                        are_hands_sorted = False
                    break

output = 0
hand_rank = 1
for hand in hands_score:
    output += hand[2] * hand_rank
    hand_rank += 1

print(output)

