import re

def get_size(dir_tree:dict[dict], dir_name:str) -> int:
    size = 0 
    for name, data in dir_tree[dir_name].items():
        if data == "dir":
            if dir_name != "":
                ndir = dir_name + "_" + name
            else:
                ndir = name
            size += get_size(dir_tree, ndir)
        else:
            size += int(data)
    return size

with open("input.txt", "r", encoding="ascii") as f:
    size_tree = {}
    cur_dir = []
    for line in f.readlines():
        if line[0] == "$":
            param = re.findall(r"^\$\s?(\w+)\s?(.+)$", line)[0]
            if param[0] == "cd":
                if param[1] == "/":
                    cur_dir = []
                elif param[1] == "..":
                    cur_dir.pop()
                else:
                    cur_dir.append(param[1])

            if param[0] == "ls":
                pass
        else:
            line = line.replace("\n", "")
            data, name = line.split(" ")
            cd_str = "_".join(cur_dir)
            if size_tree.get(cd_str, None) is None:
                size_tree[cd_str] = {}

            size_tree[cd_str][name] = data

    total_size = 0
    for dirname in size_tree.keys():
        if (size := get_size(size_tree, dirname)) <= 100000:
            total_size += size
    print(f"Total size of all directories below size 100,000: {total_size}")

    space_left = 70_000_000-get_size(size_tree, "")
    need_to_clear = 30_000_000 - space_left 

    sml_found = None
    for dirname in size_tree.keys():
        if (dir_size := get_size(size_tree, dirname)) >= need_to_clear:
            if sml_found is None or dir_size < sml_found:
                sml_found = dir_size
    print(f"Size of smallest directory to remove: {sml_found}")