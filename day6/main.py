with open("input.txt", "r", encoding="ascii") as f:
    chq = []
    cnt = 0
    while True:
        ch = f.read(1)
        cnt += 1
        if not ch:
            break

        if len(chq) != 4:
            chq.append(ch)
        else:
            if len(set(chq)) == len(chq):
                print("Start of packet: "+cnt-1)
                break
            else:
                chq.pop(0)
                chq.append(ch)

with open("input.txt", "r", encoding="ascii") as f:
    chq = []
    cnt = 0
    while True:
        ch = f.read(1)
        cnt += 1
        if not ch:
            break

        if len(chq) != 14:
            chq.append(ch)
        else:
            if len(set(chq)) == len(chq):
                print("Start of message: "+cnt-1)
                break
            else:
                chq.pop(0)
                chq.append(ch)