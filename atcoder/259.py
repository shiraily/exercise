def growth():
    n, m, x, t, d = list(map(int, input().split()))

    if m >= x:
        return t
    return t - d * (x - m)


# print(growth())

# import math

def clock():
    a, b, d = list(map(int, input().split()))
    d2 = math.radians(d)
    cos = math.cos(d2)
    sin = math.sin(d2)
    a2 = cos * a - sin * b
    b2 = sin * a + cos * b
    print("{} {}".format(a2, b2))


# clock()


def xxx():
    s = input() + "!"
    t = "!" + input()

    j = 0
    max_t = len(t) - 1
    is_invalid = False
    serial_s = 1
    prev_ss = "!"
    for i in range(len(s)):
        if j > max_t:
            is_invalid = True
            break

        ss = s[i]
        if ss == prev_ss:
            serial_s += 1
            continue

        # prev_ssの連続の処理
        init_t = t[j]
        if init_t != prev_ss:
            is_invalid = True
            break
        serial_t = 0
        while j <= max_t and t[j] == init_t:
            serial_t += 1
            j += 1
        if (serial_s == 1 and serial_t > 1) or serial_s > serial_t:
            is_invalid = True
            break

        serial_s = 1
        prev_ss = ss

    if is_invalid:
        return "No"
    if j <= max_t:
        return "No"
    return "Yes"


# print(xxx())


import math


def get_circles():
    n = int(input())
    sx, sy, tx, ty = list(map(int, input().split()))
    circles = []  # [(x, y, r)]
    for i in range(n):
        circles.append(tuple(map(int, input().split())))

    circle_grps = []  # [{1, 2}, {3, 5}, ...]
    s_circle = -1
    t_circle = -1

    for i in range(n):
        x, y, r = circles[i]

        # start, endを探す
        d_s = math.sqrt((x - sx) ** 2 + (y - sy) ** 2)
        if d_s == r:
            s_circle = i
        d_t = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
        if d_t == r:
            t_circle = i

        # 重なっている円をグループにまとめる
        in_grp = False
        for grp in circle_grps:
            if in_grp:
                break
            for c in grp:
                x2, y2, r2 = circles[c]
                d = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                rr = r + r2
                if d == rr or abs(r - r2) <= d <= rr:
                    in_grp = True
                    grp.add(i)
                    break
        if not in_grp:
            circle_grps.append({i})

    if next(grp for grp in circle_grps if s_circle in grp) \
            == next(grp for grp in circle_grps if t_circle in grp):
        return "Yes"
    return "No"


