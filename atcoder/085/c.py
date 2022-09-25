def c():
    n, Y = list(map(int, input().split()))
    y = Y // 1000

    flag = False
    n_x = -1
    n_y = -1
    n_z = -1

    max_x = min(n, y // 10)
    for i in range(0, max_x):
        n_x = max_x - i
        if (y - n - (9 * n_x)) % 4 == 0:
            n_y = (y - n - (9 * n_x)) // 4
            if n_y >= 0 and (n - n_x - n_y) >= 0:
                flag = True
                break

    if flag:
        print(n_x, n_y, n - n_x - n_y)
    else:
        print("-1 -1 -1")

c()