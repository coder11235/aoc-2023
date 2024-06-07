def get_relevant(line: str):
    _, line = line.split(":")
    return list(map(
        lambda chr: int(chr),
        list(filter(
            lambda chr: chr != "",
            line.split(" ")
        ))
    ))


def parse(real_inp):
    file_nm = "input.txt" if real_inp else "sample.txt"
    raw = open(file_nm).read().splitlines()
    
    data = list(map(get_relevant, raw))
    zipped = []
    for i in range(len(data[0])):
        zipped.append((data[0][i], data[1][i]))
    return zipped