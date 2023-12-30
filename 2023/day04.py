def get_nb_matches_card(card):
    winning_numbers, numbers_i_have = card.split(":")[1].split("|")
    winning_numbers = winning_numbers.split(" ")
    numbers_i_have = numbers_i_have.split(" ")
    winning_numbers = list(filter(None, winning_numbers))
    numbers_i_have = list(filter(None, numbers_i_have))
    numbers_i_have[-1] = numbers_i_have[-1].replace('\n', '')
    matches = [number_i_have in winning_numbers for number_i_have in numbers_i_have ]
    sum_matches = sum(matches)
    return sum_matches

# Sum of points
output_part_1 = 0
# Total number of cards
output_part_2 = 0

# Dictionary of scratchcards. Key = card index, value = [ nb_matches, nb copies (at least 1) ]
cards_dict = dict()

card_ind = 0
for line in open("input_d04"):
    sum_matches = get_nb_matches_card(line)
    cards_dict[card_ind] = [ sum_matches, 1 ]
    if sum_matches > 0:
        score_card = pow(2, sum_matches - 1)
        output_part_1 += score_card
    card_ind += 1

for card_ind, [ nb_matches, nb_copies ] in cards_dict.items():
    for _ in range(0, nb_copies):
        for i in range(0, nb_matches):
            cards_dict[card_ind + i + 1][1] += 1
        output_part_2 += 1

print(output_part_1)
print(output_part_2)
