
problematic = 0
with open("example.txt", "r", encoding="ascii") as f:
    for line in f.readlines():
        pairs = [list(map(int,pair.split("-"))) for pair in line.replace("\n","").split(",")]

        if pairs[0][0] <= pairs[1][0]:
            ind_sml = 0
            ind_bgr = 1
        else:
            ind_sml = 1
            ind_bgr = 0

        if pairs[ind_sml][1] >= pairs[ind_bgr][1]:
            problematic += 1

print(problematic)