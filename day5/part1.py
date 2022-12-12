import re

with open("input.txt", "r", encoding="ascii") as f:
    cargo:list[list[str]] = []
    matched:bool = False
    stacks:list = []
    for line in f.readlines():
        if not matched:
            if re.match(r"^( \d  ?)+$", line):
                matched = True

                # stack_cnt = int(line[~2])-1

                # Transpose by 90°                    
                cargo = list(map(list, zip(*cargo)))

                for stack in cargo:
                    stack = [x for x in stack if x != ' ']
                    stack.reverse()
                    stacks.append(stack)
                continue
            else:
                tmp = re.findall(r"((?:\[\w\])|(?:\s{3}))\s?", line)
                cargo.append([x[1] for x in tmp])
        else:
            instr = re.findall(r"^move (\d+) from (\d+) to (\d+)$", line)
            if len(instr) != 1: 
                continue

            quant, stFrom, stTo = map(int,instr[0])

            for _ in range(quant):
                cur = stacks[stFrom-1].pop()

                stacks[stTo-1].append(cur)
    out = [stack[-1] for stack in stacks]
    print(*out,sep="")