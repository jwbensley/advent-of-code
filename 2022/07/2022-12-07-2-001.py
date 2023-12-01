file_tree = { "d:/": { "p:": "d:/" } }
cur_dir = file_tree["d:/"]
cur_dir_name = "d:/"
running_ls = False
for line in open("input"):
    if line[0] == "$":
        if running_ls:
            running_ls = False
        cmd = line.split()[1]
        if cmd == "cd":
            new_dir = f"d:{line.split()[2]}"
            if new_dir == "d:/":
                cur_dir_name = "d:/"
                cur_dir = file_tree[cur_dir_name]
            elif new_dir == "d:..":
                cur_dir = cur_dir["p:"]
            else:
                cur_dir = cur_dir[new_dir]
                cur_dir_name = new_dir
        elif cmd == "ls":
            running_ls = True
    else:
        if line.split()[0] == "dir":
            new_dir = f"d:{line.split()[1]}"
            if new_dir not in cur_dir:
                cur_dir[new_dir] = {"p:": cur_dir}
                cur_dir_name = new_dir
        else:
            cur_dir[f"f:{line.split()[1]}"] = int(line.split()[0])

total_space = 70000000
required_space = 30000000
def find_total(cur_dir):
    dir_total = 0
    for x in cur_dir:
        if x[:2] == "f:":
            dir_total += cur_dir[x]
        elif x[:2] == "d:":
            dir_total += find_total(cur_dir[x])

    cur_dir["s:"] = dir_total
    return dir_total
used_space = find_total(file_tree["d:/"])
free_space = total_space - used_space
need_to_free = required_space - free_space

def find_smallest(cur_dir, smallest):
    for x in cur_dir:
        if x[:2] == "d:":
            if cur_dir[x]["s:"] >= need_to_free:
                if cur_dir[x]["s:"] < smallest:
                    smallest = cur_dir[x]["s:"]
                sub_dir = find_smallest(cur_dir[x], smallest)
                if sub_dir < smallest:
                    smallest = sub_dir
    return smallest

print(find_smallest(file_tree["d:/"], used_space))
