raw = open("input.txt").readlines()

def p1():
    ans = 0
    for line in raw:
        nums = ""
        for chr in line:
            if chr.isdigit():
                nums += chr
        ans += int(nums[0] + nums[-1])
    return ans

word_digs = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

words_digs_rev = {}

def generate_reversed():
    for wrd, dig in word_digs.items():
        words_digs_rev["".join(reversed(wrd))] = dig

def p2():
    generate_reversed()
    ans = 0
    for line in raw:
        min_dig = None
        min_pos = float("inf")
        max_dig = None
        max_pos = -1

        # find first pos dig
        for i in range(1,10):
            pos = line.find(str(i))
            if pos == -1:
                continue
            if pos < min_pos:
                min_dig = i
                min_pos = pos

        # find first pos wrd
        for wrd in word_digs:
            pos = line.find(wrd)
            if pos == -1:
                continue
            if pos < min_pos:
                min_dig = word_digs.get(wrd)
                min_pos = pos

        rev_line = "".join(reversed(line))
        # find last pos dig
        for i in range(1,10):
            pos = rev_line.find(str(i))
            if pos == -1:
                continue
            pos = len(line) - pos - 1
            if pos > max_pos:
                max_dig = i
                max_pos = pos

        # find last pos wrd
        for wrd in words_digs_rev:
            pos = rev_line.find(wrd)
            if pos == -1:
                continue
            pos = len(line) - pos - 1
            if pos > max_pos:
                max_dig = words_digs_rev.get(wrd)
                max_pos = pos
        
        num = int(str(min_dig) + str(max_dig))
        ans += num
    return ans

print(p2())