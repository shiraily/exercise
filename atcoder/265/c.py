def dir_to_idx(dir, current, h, w):
    r, c = _dir_to_idx(dir, current)
    if r == 0 or r == h + 1 or c == 0 or c == w + 1:
        return -1
    return r, c


def _dir_to_idx(dir, current):
    r, c = current
    if dir == "U":
        return r - 1, c
    elif dir == "D":
        return r + 1, c
    elif dir == "L":
        return r, c - 1
    else:
        return r, c + 1


def c():
    h, w = list(map(int, input().split()))

    init_row = [" "] * (w + 2)
    matrix = [init_row]
    for i in range(h):
        row = " " + input() + " "
        matrix.append(row)
    matrix.append(init_row)

    #  print(matrix)

    current = (1, 1)
    paths = {current}
    has_loop = False

    while True:
        direction = matrix[current[0]][current[1]]
        ret = dir_to_idx(direction, current, h, w)
        if ret == -1:
            break
        if ret in paths:
            has_loop = True
            break
        paths.add(ret)
        current = ret

    if has_loop:
        print("-1")
    else:
        print(current[0], current[1])


c()
