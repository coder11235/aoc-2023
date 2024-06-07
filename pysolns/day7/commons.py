def parse(is_actual):
    fl_name = "input.txt" if is_actual else "sample.txt"
    raw = open(fl_name).read().splitlines()
    parsed = []
    for line in raw:
        hand, bid = line.split(" ")
        bid = int(bid)
        parsed.append((hand, bid))
    return parsed