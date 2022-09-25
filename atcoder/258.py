def samp():
    n = int(input())
    if n < 60:
        return "21:{}".format(str(n).zfill(2))
    else:
        a = str(n - 60)
        return "22:{}".format(a.zfill(2))

# print(samp())
# print(samp())
# print(samp())

def get_num(i, j, n):
    candidates = []  # (ii, jj)
    max_num = -1
    for ii in range(3):
        for jj in range(3):
            if ii == 1 and jj == 1:
                continue
            iii = ii - 1
            jjj = jj - 1
            tgt = arr[iii][jjj]
            if tgt > max_num:
                candidates = [(iii, jjj)]
                max_num = tgt
            if tgt == max_num:
                candidates.append((iii, jjj))
    if n == 1:
        return max_num
    multiple = 10 ** (n - 1)
    return list(map(lambda x: multiple * max_num + get_num(x[0], x[1], n-1), candidates))


from collections import defaultdict

def narr(buf):
    lines = buf.split("\n")
    n = int(lines[0])
    arr = []
    for i in range(n):
        arr.append(list(map(int, list(lines[i + 1]))))

    max_num = -1
    paths = []  # [[(), (), ()], [], ...]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_num:
                paths = [[(i, j)]]
                max_num = arr[i][j]
            elif arr[i][j] == max_num:
                paths.append([(i, j)])

    ret = [max_num]
    nn = n
    while nn > 1:
        path_candidates = defaultdict(list)
        max_num = -1
        for i, path in enumerate(paths):
            prev_coords = set(path)
            for ii in range(3):
                for jj in range(3):
                    iii = (ii - 1 + path[-1][0]) % n
                    jjj = (jj - 1 + path[-1][1]) % n
                    coord = (iii, jjj)
                    if coord in prev_coords:
                        # ii == 1, jj == 1も弾かれる
                        continue
                    val = arr[iii][jjj]
                    if val > max_num:
                        path_candidates[i] = [coord]
                        max_num = val
                    elif val == max_num:
                        path_candidates[i].append(coord)
        new_paths = []
        for i, cands in path_candidates.items():
            if arr[cands[0][0]][cands[0][1]] == max_num:
                new_paths.extend(list(map(lambda c: paths[i] + [c], cands)))
        paths = new_paths
        ret.append(max_num)
        nn -= 1
    print("".join(list(map(str, ret))))

narr(
"""4
1161
1119
7111
1811"""
)


narr(
"""4
1111
1111
1111
1111"""
)

narr(
    """1
1"""
)

narr(
    """2
11
11"""
)

narr(
"""4
9191
8181
7771
3333"""
)
"""
A: (0,0), (1,0), (2,1) to (1,2)
B: (0,2), (1,2), (2,1) to (1,0)
"""