elfs = [0]

with open("input.txt", "r", encoding="ascii") as f:
    for line in f.readlines():
        if line == "\n":
            elfs.append(0)
        else:
            elfs[-1] += int(line)
elfs = sorted(elfs)


print(f"Top elf: {elfs[-1]}")
print(f"Sum of top 3 elfs: {sum(elfs[-3:])}")
