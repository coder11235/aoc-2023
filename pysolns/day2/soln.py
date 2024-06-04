raw = open("input.txt").read().splitlines()

def parse():
    games = []
    for line in raw:
        _, games_raw = line.split(": ")
        indiv_game_round = games_raw.split("; ")
        game_rounds = []
        for round_raw in indiv_game_round:
            game_round = {}
            clr_drs = round_raw.split(", ")
            for clr_dr in clr_drs:
                num, color = clr_dr.split(" ")
                game_round[color] = int(num)
            game_rounds.append(game_round)
        games.append(game_rounds)
    return games

games_parsed = parse()

def p1():
    ans = 0
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for game_id, game in enumerate(games_parsed):
        is_game_valid = True
        game_id += 1
        for round in game:
            for color, num_cubes in round.items():
                if max_cubes[color] < num_cubes:
                    is_game_valid = False
                    break
            if not is_game_valid:
                break
        if is_game_valid:
            ans += game_id
    return ans

def p2():
    ans = 0
    for game_id, game in enumerate(games_parsed):
        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in game:
            for color, num_cubes in round.items():
                if max_cubes[color] < num_cubes:
                    max_cubes[color] = num_cubes
        game_pow = 1
        for _, v in max_cubes.items():
            game_pow *= v
        ans += game_pow
    return ans
            
print(p2())