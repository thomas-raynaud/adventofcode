def sort_hands(i_hands, order, score_col_ind):
    hands = i_hands.copy()
    are_hands_sorted = False
    while not are_hands_sorted:
        are_hands_sorted = True
        for i in range(1, len(hands)):
            if hands[i - 1][score_col_ind] < hands[i][score_col_ind]:
                hands[i - 1], hands[i] = hands[i], hands[i - 1]
                are_hands_sorted = False
            elif hands[i - 1][score_col_ind] == hands[i][score_col_ind]:
                for a, b in zip(list(hands[i - 1][0]), list(hands[i][0])):
                    if order.index(a) == order.index(b):
                        continue
                    else:
                        if order.index(a) < order.index(b):
                            hands[i - 1], hands[i] = hands[i], hands[i - 1]
                            are_hands_sorted = False
                        break
    return hands


def sort_cards(hand):
    hand_sorted = hand.copy()
    is_hand_sorted = False
    while not is_hand_sorted:
        is_hand_sorted = True
        for i in range(1, len(hand_sorted)):
            if order.index(hand_sorted[i - 1]) > order.index(hand_sorted[i]):
                hand_sorted[i - 1], hand_sorted[i] = hand_sorted[i], hand_sorted[i - 1]
                is_hand_sorted = False
    return hand_sorted


def get_score(hand):
    prev_x = hand[0]
    occurences = []
    curr_occurence = 1
    for x in hand[1:]:
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
    return score


order = [ "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]
order_p2 = [ "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J" ]
hands_score = []

for line in open("input_d07"):
    hand, bid = line.rstrip().split(" ")
    hand = list(hand)
    bid = int(bid)

    hand_sorted = sort_cards(hand)
    score = get_score(hand_sorted)

    try:
        max_card = max([ x for x in hand_sorted if x != "J" ], key=hand_sorted.count)
    except ValueError:
        # All cards are jokers
        max_card = "A"
    hand_p2 = list(map(lambda x: x.replace("J", max_card), hand_sorted))
    hand_p2 = sort_cards(hand_p2)
    score_p2 = get_score(hand_p2)
    hands_score.append([ ''.join(hand), score, score_p2, bid ])

hands_sorted_p1 = sort_hands(hands_score, order, 1)
hands_sorted_p2 = sort_hands(hands_score, order_p2, 2)

output_p1 = 0
output_p2 = 0
hand_rank = 1
for hand_p1, hand_p2 in zip(hands_sorted_p1, hands_sorted_p2):
    output_p1 += hand_p1[3] * hand_rank
    output_p2 += hand_p2[3] * hand_rank
    hand_rank += 1

print(output_p1)
print(output_p2)
