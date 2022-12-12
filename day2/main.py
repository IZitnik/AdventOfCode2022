
score = 0
lookup_win = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6}
}
with open("input.txt", "r", encoding="ascii") as f:
    for line in f.readlines():
        op_ch, my_ch = line.replace("\n", "").split(" ")

        score += lookup_win[op_ch][my_ch]
print(f"part1 score: {score}")


score = 0
lookup_outc = {
    "A": {"X": 3, "Y": 4, "Z": 6+2},
    "B": {"X": 1, "Y": 5, "Z": 6+3},
    "C": {"X": 2, "Y": 6, "Z": 6+1}
}
with open("input.txt", "r", encoding="ascii") as f:
    for line in f.readlines():
        op_ch, outcome = line.replace("\n", "").split(" ")

        score += lookup_outc[op_ch][outcome]
print(f"part2 score: {score}")
