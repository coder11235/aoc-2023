raw = open("input.txt").read().splitlines()
import math

def parse_sec(portion: str) -> set[int]:
    parsed = set(portion.split(" "))
    if "" in parsed:
        parsed.remove("")
    parsed = set([int(el) for el in parsed])
    return parsed

def parse() -> list[int]:
    cards = []
    for line in raw:
        _, line = line.split(":")
        left, right = line.split(" | ")
        winning = parse_sec(left)
        obtained = parse_sec(right)
        inter = winning.intersection(obtained)
        cards.append(len(inter))
    return cards

parsed_data = parse()

def p1():
    ans = 0
    for i in parsed_data:
        ans += math.floor(math.pow(2, i-1))
    return ans

def p2():
    # generate number of cards
    parsed_mod = dict()
    for card_no, i in enumerate(parsed_data):
        parsed_mod[card_no+1] = [1, i]
    for card_no, arr in parsed_mod.items():
        count = arr[0]
        inter_len = arr[1]
        for next_c in range(card_no+1, card_no+inter_len+1):
            parsed_mod[next_c][0] += count

    # find sum of num of cards
    ans = 0
    for _, arr in parsed_mod.items():
        ans += arr[0]
    return ans


print(p2())