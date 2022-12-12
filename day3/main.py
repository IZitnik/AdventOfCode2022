prio = 0
with open("input.txt", "r", encoding="ascii") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        first, sec = line[:len(line)//2], line[len(line)//2:]

        common = [val for val in first if val in sec][0]
        prio += ord(common) - (96 if "a" <= common <= "z" else 38)
print(prio)
    
prio = 0
with open("input.txt", "r", encoding="ascii") as f:
    group = []
    for line in f.readlines():
        group.append(line.replace("\n", ""))
        if len(group) == 3:
            common = [chr for chr in group[0] if chr in group[1] and chr in group[2]][0]
            prio += ord(common) - (96 if "a" <= common <= "z" else 38)
            group = []
print(prio)