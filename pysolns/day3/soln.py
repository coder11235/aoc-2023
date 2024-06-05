raw = open("input.txt").read().splitlines()

def parse():
    matrix = []
    for line in raw:
        row = []
        for chr in line:
            row.append(chr)
        matrix.append(row)
    return matrix

matrix = parse()

is_symbol = lambda char: not (char.isdigit() or char == ".")

def gen_near_rel():
    arr = [-1,0,1]
    near_rel = []
    for i in arr:
        for j in arr:
            near_rel.append((i, j))
    return near_rel

near_rel = gen_near_rel()

def check_vicinity_symb(matrix, row_ind, col_ind):
    for i, j in near_rel:   
        near_row = row_ind+i
        near_col = col_ind+j
        try:
            if is_symbol(matrix[near_row][near_col]):
                return True
        except:
            continue
    return False


def p1():
    part_num = []
    for row_ind, row in enumerate(matrix):
        current_number = 0
        is_part_num = False
        for chr_ind, chr in enumerate(row):
            if chr.isdigit():
                current_number = current_number*10 + int(chr)
                if not is_part_num:
                    is_part_num = check_vicinity_symb(matrix, row_ind, chr_ind)
            else:
                if current_number != 0:
                    if is_part_num:
                        part_num.append(current_number)
                    current_number = 0
                    is_part_num = False
        if current_number != 0:
            if is_part_num:
                part_num.append(current_number)
    return sum(part_num)

def check_vicinity_gear(matrix: list[list[int]], row_ind: int, col_ind: int, gear_pos_set: set[(int, int)]):
    gear_positions = set()
    for i, j in near_rel:   
        near_row = row_ind+i
        near_col = col_ind+j
        try:
            if matrix[near_row][near_col] == "*":
                gear_positions.add((near_row, near_col))
                gear_pos_set.add((near_row, near_col))
        except:
            continue
    return gear_positions

def get_num_gear_rels():
    num_gear_rels = []
    gear_pos_set = set()
    for row_ind, row in enumerate(matrix):
        current_number = 0
        linked_gears = set()
        for col_ind, chr in enumerate(row):
            if chr.isdigit():
                current_number = current_number*10 + int(chr)
                linked_gears = linked_gears.union(check_vicinity_gear(matrix, row_ind, col_ind, gear_pos_set))
            else:
                if current_number != 0:
                    num_gear_rels.append((current_number, linked_gears))
                    linked_gears = set()
                    current_number = 0
        if current_number != 0:
            num_gear_rels.append((current_number, linked_gears))
    return (num_gear_rels, gear_pos_set)

def p2():
    num_gear_rels, gear_pos_set = get_num_gear_rels()
    ans = 0
    for gear_pos in gear_pos_set:
        linked_nums = []
        for num, linked_gears in num_gear_rels:
            if gear_pos in linked_gears:
                linked_nums.append(num)
        if len(linked_nums) == 2:
            ans += linked_nums[0] * linked_nums[1]
    return ans


print(p2())