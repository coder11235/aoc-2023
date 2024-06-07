import commons, functools

parsed = commons.parse(True)

# compare cards
card_list: list = ["J"] + list([str(c) for c in range(2,10)]) + ["T", "Q", "K", "A"]
def cmp_letter(c1, c2):
    if len(c1) == 0:
        return 0
    i1 = card_list.index(c1)
    i2 = card_list.index(c2)
    if i1 < i2:
        return -1
    elif i1 == i2:
        return 0
    else:
        return 1
    
# compare hand if same type
def cmp_same_type(h1, h2):
    l1 = h1[0]
    l2 = h2[0]
    letter_cmp = cmp_letter(l1, l2)
    if letter_cmp == 0:
        return cmp_same_type(h1[1:], h2[1:])
    else:
        return letter_cmp

def get_hand_score_new(hand: str):
    scores = []
    for chr in card_list:
        scores.append(get_hand_score(hand.replace("J", chr)))
    return max(scores)

# get base hand score
def get_hand_score(hand: str):
    hand_set = set(hand)
    count_set = set()
    for i in hand_set:
        count_set.add(hand.count(i))

    if len(hand_set) == 1:
        return 6
    if len(hand_set) == 2:
        cnt = hand.count(hand[0])
        if cnt == 1 or cnt == 4:
            return 5
        else:
            return 4
    if len(hand_set) == 5:
        return 0
    if len(hand_set) == 4:
        return 1
    return 2 if count_set == {1, 2} else 3

# fully compare hands
def cmp_hand_type(h1_c, h2_c):
    h1_score = get_hand_score_new(h1_c[0])
    h2_score = get_hand_score_new(h2_c[0])
    if h1_score < h2_score:
        return -1
    elif h1_score > h2_score:
        return 1
    else:
        return cmp_same_type(h1_c[0], h2_c[0])
    
hands_ranked = sorted(parsed, key=functools.cmp_to_key(cmp_hand_type))

ans = 0

for rank, (_, bid) in enumerate(hands_ranked):
    rank = rank+1
    ans += rank * bid

print(ans)