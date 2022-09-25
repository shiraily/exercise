def b():
    s_arr = [input() for _ in range(10)]

    a = 1
    for i, s in enumerate(s_arr):
        if "#" in s:
            a = i + 1
            break

    b = 1
    for i, s in enumerate(s_arr):
        if "#" in s:
            b = i + 1

    c = s_arr[a - 1].index("#") + 1
    d = s_arr[a - 1].rindex("#") + 1

    print("{} {}".format(a, b))
    print("{} {}".format(c, d))

b()

