from collections import defaultdict

def full_house():
    cards = list(map(int, input().split()))

    d = defaultdict(int)

    for c in cards:
        d[c] += 1

    has_two = False
    for v in d.values():
        if v == 2:
            has_two = True
    if len(d) == 2 and has_two:
        print("Yes")
    else:
        print("No")

# full_house()


from collections import defaultdict

def ancestor():
    n = int(input())
    # P2 to Pn
    ps = list(map(int, input().split()))

    d = defaultdict(int)

    for i, p in enumerate(ps):
        ii = i + 2
        d[ii] = p

    parent = n
    counter = 0
    while parent != 1:
        parent = d[parent]
        counter += 1

    print(counter)

# ancestor()


# import copy

def mono():
    n, m = list(map(int, input().split()))

    arr = [i + 1 for i in range(n)]
    print(" ".join(list(map(str, arr))))
    while arr != [m - n + i + 1 for i in range(n)]:
        print(" ".join(list(map(str, get_next(arr, n, m)))))


def get_next(arr, n, m):
    tgt_idx = -1
    for j in range(n):
        idx = n - j - 1
        if arr[idx] < m - j:
            tgt_idx = idx
            break
    new_arr = arr

    tgt_val = new_arr[tgt_idx] + 1
    new_arr[tgt_idx] = tgt_val
    for j in range(tgt_idx + 1, n):
        tgt_val += 1
        new_arr[j] = tgt_val
    return new_arr

# mono()


def lr(s1, s2):
    n, l, r = list(map(int, s1.split()))
    arr = list(map(int, s2.split()))  # a1, a2, ..., an

    if n == 1:
        return min(arr[0], l, r)

    sum_x = 0
    sum_y = 0
    max_sum_x = 0
    max_sum_y = 0
    ret_naive_x = -1
    ret_naive_y = n
    for x in range(n):
        ax = arr[x]
        sum_x += ax
        """
        置換する価値あり
        今見ているところがlより大きい
        前回のmaxとの差分が、n * lより大きい
        """
        if ax > l and (sum_x - max_sum_x) > (x - ret_naive_x) * l:
            max_sum_x = sum_x
            ret_naive_x = x

        y = n - x - 1
        ay = arr[y]
        sum_y += ay
        if ay > r and (sum_y - max_sum_y) > (ret_naive_y - y) * r:
            max_sum_y = sum_y
            ret_naive_y = y

    # print("ret", ret_naive_x, ret_naive_y)

    ret_x = -1
    ret_y = n
    if ret_naive_x >= ret_naive_y:
        sum_x = 0
        max_sum_x = 0
        for x in range(ret_naive_y):
            ax = arr[x]
            sum_x += ax
            if ax > l and (sum_x - max_sum_x) > (x - ret_x) * l:
                max_sum_x = sum_x
                ret_x = x

        sum_y = 0
        max_sum_y = 0
        init_y = ret_naive_x + 1
        for i in range(init_y, n):
            y = n - 1 + init_y - i
            ay = arr[y]
            sum_y += ay
            # print("y=", ay, "sum=", sum_y)
            if ay > r and (sum_y - max_sum_y) > (ret_y - y) * r:
                max_sum_y = sum_y
                ret_y = y

    # print("ret", ret_x, ret_y)

    # 0のとき考慮していない?
    if ret_naive_x + 1 < ret_naive_y:
        s_mid = sum(arr[ret_naive_x+1: ret_naive_y])
        # print("easy")
        return (ret_naive_x + 1) * l + (n - ret_naive_y) * r + s_mid
    elif ret_naive_x + 1 == ret_naive_y:
        # print("min")
        return min(l * n, r * n, sum(arr))
    else:
        l_or_r = min(l * n, r * n, sum(arr))
        r1 = l * (ret_naive_x + 1) + sum(arr[ret_naive_x+1:ret_y]) + (n - ret_y) * r
        r2 = l * (ret_x + 1) + sum(arr[ret_x+1:ret_naive_y]) + (n - ret_naive_y) * r
        # print("else", l_or_r, r1, r2)
        return min(l_or_r, r1, r2)


# print(lr(input(), input()))

def pp(i1, i2, expected):
    ret = lr(i1, i2)
    if ret != expected:
        print("!", i1, "/", i2)
        print(ret, expected)

# sample
pp(
    "5 4 3",
    "5 5 0 6 3",
    14)

pp(
    "4 10 10",
    "1 2 3 4",
    10)

pp(
    "10 -5 -3",
    "9 -6 10 -1 2 10 -1 7 -15 5",
    -58)

# 1 number
pp(
    "1 -1 4",
    "0",
    -1)

pp(
    "1 -1 -2",
    "0",
    -2)

pp(
    "1 1 1",
    "-100",
    -100)

pp(
    "1 -98 -97",
    "-1000",
    -1000)

pp(
    "1 -198 -197",
    "-100",
    -198)

# 2 numbers
pp(
    "2 3 8",
    "4 2",
    5)

pp(
    "2 8 8",
    "1 1",
    2)

pp(
    "2 1 2",
    "0 98",
    2)

pp(
    "2 1 2",
    "99 98",
    2)

pp(
    "2 1 2",
    "-100 -200",
    -300)

pp(
    "2 -300 -400",
    "-100 -200",
    -800)

pp(
    "2 -300 -300",
    "-100 -200",
    -600)

#
# それ以降
#

# 正順
pp(
    "5 4 3",
    "2 107 -100 4 3",
    -86)

pp(
    "5 4 3",
    "10 -100 -100 -100 10",
    -293)

# xのみ
pp(
    "5 3 3",
    "10 3 3 10 1",
    13)

# yのみ
pp(
    "5 3 3",
    "1 10 3 3 10",
    13)

# 真ん中かぶりでxなし,y途中
pp(
    "5 8 3",
    "3 2 100 4 1",
    14)

# 真ん中かぶりでyなし、x途中
pp(
    "5 3 4",
    "2 1 100 0 5",
    13)

# all left
pp(
    "4 2 3",
    "3 4 5 6",
    8)

# all right
pp(
    "4 3 2",
    "9 4 5 6",
    8)

pp(
    "5 1000 3",
    "2 107 -100 4 3",
    14)

# all is replaced with minus
pp(
    "5 -10 -20",
    "2 107 -10 4 3",
    -100)

pp(
    "5 0 0",
    "0 0 0 0 0",
    0)

